from flask import Flask
from flask_pymongo import PyMongo
import yaml

app = Flask(__name__)
db = yaml.load(open('db.yaml'))
app.config['MONGO_DBNAME'] = db['mongo_alchamy_db']
app.config['MONGO_URI'] = db['mongo_alchamy_connection']

mongo = PyMongo(app)


@app.route('/add')
def add():
    user = mongo.db.actor  # Here actor is a table and sakila from db.yaml is database
    user.insert({'name': 'Antony', 'age': 20})
    user.insert({'name': 'Antony', 'language': 'Python'})
    user.insert({'name': 'Kelly', 'language': 'C'})
    user.insert({'name': 'John', 'language': 'Java'})
    user.insert({'name': 'Cedric', 'language': 'Haskell'})
    return 'Added multiple users!!'


@app.route('/find')
def find():
    user = mongo.db.actor
    john = user.find_one({'name': 'John'})
    return 'You found ' + john['name'] + '. His favorite languase is ' + john['language']


@app.route('/update')
def update():
    user = mongo.db.actor
    john = user.find_one({'name': 'John'})
    john['language'] = 'Ruby'
    user.save(john)
    return 'Update users language'


@app.route('/delete')
def delete():
    user = mongo.db.actor
    kelly = user.find_one({'name': 'Kelly'})
    user.remove(kelly)
    return 'Removed Kelly!!'


app.run(debug=True)