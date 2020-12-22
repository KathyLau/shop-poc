from flask import Flask, render_template, request, jsonify
from utils.setup import selectshopbyname, selectshops, selectdefaultshops
from utils.store import insert, countSuggestionsInDB
app = Flask(__name__)

searchterm = "Search Results"
api_key = "AIzaSyD43vlw78-rgjz6a5iczPSEDO1bxQC9hZ0"

bizlist = selectdefaultshops()
returnlist = []
searchlist = []
suggestionlist = []
suggestionlistlength = 0


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return render_template('index.html')
    else:
        bizlist = selectdefaultshops()
        return render_template('index.html', API_KEY=api_key, searchlist=bizlist)  # noqa: E501


@app.route('/restaurant')
def restaurant(name=None):
    return render_template('index.html', data='data')


# handles search bar searches
@app.route('/search/', methods=['GET', 'POST'])
def search():
    global bizlist
    global returnlist
    global searchlist
    global searchterm

    returnlist.clear()
    searchlist.clear()

    searchterm = request.args.get('s').lower()
    shops = selectshops(searchterm) + selectshopbyname(searchterm)
    for shop in shops:
        searchlist.append({
            "address": [shop[6], shop[7]],
            "id": shop[0],
            "image": shop[2],
            "name": shop[1],
            "service": shop[4],
            "text": shop[3],
            "location": shop[5],
            "type": "Restaurant"
        })
    bizlist = searchlist

    return render_template('matches.html', searchterm=searchterm, bizlist=bizlist, searchlist=searchlist, returnlist=returnlist, API_KEY=api_key)  # noqa: E501


# renders search results page
@app.route('/view/<id>', methods=['GET', 'POST'])
def view(id=id):
    global bizlist
    global returnlist
    returnlist.clear()
    list_entry = int(id)
    for (index, place) in enumerate(bizlist):
        if place["id"] == list_entry:
            returnlist.append(place)
            break
    return render_template('view.html', returnlist=returnlist)


# renders create page
@app.route('/create', methods=['GET', 'POST'])
def create(name=None):
    global bizlist
    return render_template('create.html', suggestionlist=suggestionlist)


# adds suggested restaurants to list
@app.route('/add', methods=['GET', 'POST'])
def add(name=None):
    global suggestionlist
    global suggestionlistlength
    suggestionlistlength = suggestionlistlength+1

    json_data = request.get_json()
    gname = json_data["name"]
    glocation = json_data["location"]
    gtext = json_data["text"]
    gservice = json_data["service"]
    gimage = json_data["image"]
    gtype = json_data["type"]

    new_entry = {
        "name": gname,
        "location": glocation,
        "text": gtext,
        "service": gservice,
        "image": gimage,
        "type": gtype
    }

    suggestionlist.append(new_entry)
    num = countSuggestionsInDB()
    number = num - 1
    insert(number, suggestionlist[-1]["name"],
           suggestionlist[-1]["image"],
           suggestionlist[-1]["text"], suggestionlist[-1]["service"],
           suggestionlist[-1]["location"], suggestionlist[-1]["type"])
    return jsonify(suggestionlist=suggestionlist)


# displays cards of the buisness
@app.route('/displaycards', methods=['GET', 'POST'])
def displaycards():
    global bizlist
    global returnlist

    returnlist.clear()

    returnlist = selectdefaultshops()
    return jsonify(returnlist=returnlist)


# login page for customers
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


# register page for customers
@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
