'''
    server.py
    The Wall Exercise for Python-Flask-MySQL
    Leif Anderson 7/15/17
'''
from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key="1337dungeon"
mysql = MySQLConnector(app, 'users')

@app.route('/')
def home():

    if 'id' not in session:
        session['id'] = 0
    if session['id'] != 0:
        return redirect('/wall')

    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    query='SELECT * FROM users WHERE email = :email'
    data = {
        'email' : request.form['log-email']
    }
    user = mysql.query_db(query, data)
    if user != []:
        if user[0]['password'] == request.form['log-password']:
            session['id'] = user[0]
            return redirect('/wall')
        else:
            flash('BAD PASSWORD!!!!')
            return redirect('/')
    else:
        flash('INVALID EMAIL!!!!')
        return redirect('/')

@app.route('/logout')
def logout():
    session['id'] = 0
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    if request.form['name'] and request.form['email'] and request.form['password'] and request.form['password'] == request.form['confirm-password']:
        query = 'INSERT into users (name, email, password, created_at, updated_at) VALUES (:name, :email, :password, NOW(), NOW())'
        data = {
            'name' : request.form['name'],
            'email' : request.form['email'],
            'password' : request.form['password']
        }
        mysql.query_db(query, data)
        flash('YOU ARE SUCCESSFUL!!')
    else:
        flash('FULL COMPLIANCE REQUIRED')
    return redirect('/')

@app.route('/wall')
def wall():

    if 'id' not in session:
        session['id'] = 0
    if session['id'] == 0:
        return redirect('/')

    query = 'SELECT * FROM comments JOIN users ON users.id = comments.user_id'

    messages = mysql.query_db(query)

    return render_template('wall.html', messages=messages)

@app.route('/submit', methods=['POST'])
def comment():
    if request.form['message']:
        query = 'INSERT INTO comments (message, user_id, created_at, update_at) VALUES (:message, :user_id, NOW(), NOW())'
        data = {
            'message' : request.form['message'],
            'user_id' : session["id"]["id"]
        }
        mysql.query_db(query, data)
    else:
        flash('ENTER A MESSAGE')

    return redirect('/wall')
app.run(debug=True)
