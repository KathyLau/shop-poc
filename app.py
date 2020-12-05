from flask import Flask, render_template, request, jsonify
from load import generate_list
app = Flask(__name__)

searchterm = "Search Results"
api_key = "AIzaSyD43vlw78-rgjz6a5iczPSEDO1bxQC9hZ0"
current_id = 4

bizlist = generate_list("data/black-owned-restaurants-nyc.csv")
bizlist[-10:]
bizlist = bizlist[::-1]

returnlist = []

searchlist = []


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return render_template('index.html')
    else:
        return render_template('index.html', API_KEY=api_key, shops=bizlist)


@app.route('/restaurant')
def restaurant(name=None):
    return render_template('index.html', data='data')


# to register a business
@ app.route('/create', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('create.html')
    elif request.method == 'POST':

        bname = request.form['bname']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        hours = request.form['hours']
        site = request.form['site']
        insta = request.form['insta']
        cuisine = request.form['cuisine']

        new_entry = {
            'bname': bname,
            'email': email,
            'phone': phone,
            'address': address,
            'hours': hours,
            'site': site,
            'insta': insta,
            'cuisine': cuisine
        }
        # code for mongodb to insert into db

        return render_template('index.html', data=new_entry)


# handles search bar searches
@app.route('/search/', methods=['GET', 'POST'])
def search():
    global bizlist
    global returnlist
    global searchlist
    global searchterm

    returnlist.clear()
    searchlist.clear()

    searchterm = request.args.get('s')
    for (index, place) in enumerate(bizlist):
        if (searchterm in place["location"]) or (searchterm in place["name"]) or (searchterm in (place["location"]).lower()) or (searchterm in (place["name"]).lower()):  # noqa: E501
            searchlist.append(place)
    return render_template('matches.html', searchterm=searchterm, bizlist=bizlist, searchlist=searchlist, returnlist=returnlist)  # noqa: E501


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


# displays cards of the buisness
@app.route('/displaycards', methods=['GET', 'POST'])
def displaycards():
    global bizlist
    global returnlist

    returnlist.clear()

    returnlist = bizlist[-10:]
    returnlist = returnlist[::-1]
    return jsonify(returnlist=returnlist)


if __name__ == '__main__':
    app.run(debug=True)
