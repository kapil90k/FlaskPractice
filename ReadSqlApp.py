import yaml
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
db = yaml.load(open('db.yaml'))

app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)


@app.route('/read_db/<id>', methods=['GET'])
def read_mysql(id):
    connection = mysql.connection
    cur = connection.cursor()
    fname = 'Kappu'
    lname = 'Temple'
    id = 100
    cur.execute('update actor set first_name = \'%s\', last_name = \'%s\' where actor_id = %d' % (fname, lname, id))
    cur.execute('insert into actor(actor_id, first_name, last_name, last_update) values(203, \'Aggu\',\'Singh\', current_timestamp)')
    rv = cur.fetchall()
    connection.commit()
    return str(rv)

app.run(debug=True)