from flask import Flask
from flask_pymongo import PyMongo
import yaml
from bson.json_util import dumps
from bson.son import SON

app = Flask(__name__)
db = yaml.load(open('db.yaml'))
app.config['MONGO_DBNAME'] = db['mongo_alchamy_db']
app.config['MONGO_URI'] = db['mongo_alchamy_connection']

mongo = PyMongo(app)


# mongoimport --db test --collection inventory --file D:\Software\mongodb\mongodb-json-files-master\mongodb-json-files-master\datasets\restaurant.json

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


@app.route('/testing')
def mytesting():
    table = mongo.db.catalog_book
    result = table.find({"status": "PUBLISH"}).count()
    # result = table.find({ "$or": [{"_id":3},{"_id":4}]} )
    return dumps(result)

@app.route("/multi_insert")
def multi_insert():
    table = mongo.db.inventory
    table.insert_many([
    {"item": "journal",
     "qty": 25,
     "size": SON([("h", 14), ("w", 21), ("uom", "cm")]),
     "status": "A"},
    {"item": "notebook",
     "qty": 50,
     "size": SON([("h", 8.5), ("w", 11), ("uom", "in")]),
     "status": "A"},
    {"item": "paper",
     "qty": 100,
     "size": SON([("h", 8.5), ("w", 11), ("uom", "in")]),
     "status": "D"},
    {"item": "planner",
     "qty": 75,
     "size": SON([("h", 22.85), ("w", 30), ("uom", "cm")]),
     "status": "D"},
    {"item": "postcard",
     "qty": 45,
     "size": SON([("h", 10), ("w", 15.25), ("uom", "cm")]),
     "status": "A"}])
    return "multiple rows have been inserted!!"


app.run(debug=True)
