from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re
import md5

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "secret"
mysql = MySQLConnector(app, 'logins')

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    if len(request.form['first_name']) < 2:
        flash('Please enter a first name!')
        return redirect('/')

    elif request.form['first_name'].isalpha() == False:
        flash("You cannot have any numbers in your first name")
        return redirect('/')

    elif request.form['last_name'].isalpha() == False:
        flash("You cannot have any numbers in your last name")
        return redirect('/')

    elif len(request.form['last_name']) <2:
        flash("Please enter a last name")
        return redirect('/')

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid email address")
        return redirect('/')

    elif len(request.form['password']) < 8:
        flash("Please enter a valid password")
        return redirect('/')

    elif len(request.form['confirm_password']) < 1:
        flash("Please confirm your password")
        return redirect('/')

    elif request.form['confirm_password'] != request.form['password']:
        flash("Passwords do not match")
        return redirect('/')

    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = md5.new(request.form['password']).hexdigest();
        confirm_password = md5.new(request.form['confirm_password']).hexdigest()

        query = "INSERT INTO logins (first_name, last_name, email, password, confirm_password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, :confirm_password, NOW(), NOW())"


        data = { 'first_name': first_name,
                  'last_name': last_name,
                  'email': email,
                  'password': password,
                  'confirm_password': confirm_password
                }

        mysql.query_db(query, data)

        return render_template('success.html', email = request.form['email'])

@app.route('/user_login', methods=['POST'])
def user_login():
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()

    query = "SELECT * FROM logins WHERE email = :email"

    data = {
        "email": email,
        "password": password
    }

    user = mysql.query_db(query, data)

    if len(user) != 0:
        hashed_password = md5.new(request.form['password']).hexdigest()

    if user[0]['password'] != hashed_password:
        flash("Incorrect password")
        return redirect('/')
    else:
        return render_template('success.html')


app.run(debug=True)
