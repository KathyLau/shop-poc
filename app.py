from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return render_template('index.html', API_KEY="api-key")
    else:
        return render_template('index.html')


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
        oname = request.form['oname']
        phone = request.form['phone']
        address = request.form['address']
        confirm = request.form['confirm']
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

        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
