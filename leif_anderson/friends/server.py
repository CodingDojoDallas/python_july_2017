from flask import Flask, request, redirect, render_template, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    friend = mysql.query_db("SELECT * FROM friendsdb")
    return render_template('index.html', friends=friend)

@app.route('/friends', methods=['POST'])
def friend():
    query = "insert into friends (name, age, created_at, updated_at) values (:name, :age, now(), now())"
    data = {
        'name': request.form['name'],
        'age': request.form['age']
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
