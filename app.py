from flask import Flask, request, jsonify
from Models.CustomerModel import *
from Models.EmployeeModel import *

# pip install flask-mysqldb
# pip install Flask-MongoAlchemy
# pip install Flask-PyMongo

app = Flask(__name__)


@app.route('/posts/')
def get_post():
    # page = request.args.get('page', 1, type=int)
    json = {
        'name': 'Kapil',
        'age': '20',
        'city': 'Bangalore',
        'state': 'Karnataka',
        'address': {
            'street': '6',
            'tahseel': 'Tundala'
        }
    }
    return jsonify(json)


@app.route('/person')
def getPerson():
    person = gettingPerson()
    return person


@app.route('/custom_person/<name>/<age>/<id>')
def getCustomPerson(name, age, id):
    person = gettingCustPerson(name, age, id)
    return person

@app.route('/my_cust', method = ['POST','GET'])
def cust_post_request():
    if request.method == 'POST':
        print(request.is_json)
        print('Lol1')
        content = request.get_json()
        response = generate_response(content)
        return response

app.run(debug=True)
