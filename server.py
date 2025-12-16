from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Home Page'
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    title = 'About Page'
    name = 'natthawut'
    email = 'myfangfc@gmail.com'
    mobile = '0653238104'
    age = 21
    return render_template('about.html',

                            name=name,
                            email=email,
                            mobile=mobile,
                            age=age)

@app.route('/favorite/foods')
def favorite_foods():
    title = 'Favorite Foods'
    foods = ['somtam', 'Kaitod', 'ping kai', 'padkapow', 'moo ping']
    return render_template('favorite_foods.html',
                            foods=foods)

@app.route('/favorite/spots')
def favorite_spots():
    title = 'Favorite Spots'
    spots = ['Football', 'Basketball', 'volleyball']
    return render_template('favorite_spots.html',
                            spots=spots)