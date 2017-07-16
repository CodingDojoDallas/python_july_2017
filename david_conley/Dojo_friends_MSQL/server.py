from flask import Flask, redirect, request, render_template, session, flash

from mysqlconnection import MySQLConnector #imports the msql connection and connector

app = Flask(__name__)
mysql = MySQLConnector(app, 'Dojo_friends')

@app.route('/')
def index():

    query = "SELECT * FROM friends" #selects table from our created database
    friends = mysql.query_db(query)  #conect to my sequal through the query

    return render_template("index.html", friends=friends)

@app.route('/addfriends', methods=["POST"])
def add():
    query = "INSERT into friends (name, age, friends_since, created_at, updated_at) values(:name, :age, :friend_since, NOW(), NOW())"
    data = {
        'name': request.form['name'],
        'age': request.form['age'],
        'friend_since': request.form['since']
        }
    mysql.query_db(query, data)

    return redirect('/')


app.run(debug=True)
