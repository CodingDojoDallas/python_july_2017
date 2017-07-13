from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "Secret"
mysql = MySQLConnector(app,'logins')

@app.route('/')
def index():
    return render_template('index.html')    

@app.route('/process', methods=['POST'])
def process():
	if len(request.form['first_name'])<2:
		flash("First name cannot be empty")
		return redirect('/')
	
	elif len(request.form['last_name'])<2:
		flash("Last name cannot be empty")
		return redirect('/')
	
	elif len(request.form['email'])<2:
		flash("Email cannot be empty")
		return redirect('/')
	
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid email address!")
		return redirect('/')
	
	elif len(request.form['password'])<2:
		flash("Password cannot be empty")
		return redirect('/')
	
	elif len(request.form['confirm_password'])<2:
		flash("Please confirm your password")
		return redirect('/')
	
	elif request.form['confirm_password'] != request.form['password']:
		flash("Passwords must match!")
		return redirect('/')

	else: 
		first_name = request.form['first_name']
		last_name = request.form['last_name']
		email = request.form['email']
		password = md5.new(request.form['password']).hexdigest();
		confirm_password = md5.new(request.form['confirm_password']).hexdigest();
		query = "INSERT INTO logins (first_name, last_name, email, password, confirm_password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, :confirm_password, NOW(), NOW())"
		 
		data = { 
		 	'first_name': first_name, 
		 	'last_name': last_name, 
		 	'email': email, 
		 	'password': password, 
		 	'confirm_password': confirm_password
		 	}

		mysql.query_db(query, data)

		return render_template('success.html', email=request.form['email'])

@app.route('/user_login', methods=['post'])
def user_login():
	email = request.form['email']
	password = md5.new(request.form['password']).hexdigest();
		
	user_query = "SELECT * FROM logins WHERE email = :email"
	query_data = {"email": email, "password": password}

	user = mysql.query_db(user_query, query_data)
	print "*"*50
	print user
	
	if len(user) != 0:
		hashed_password = md5.new(request.form['password']).hexdigest();
		if user[0]['password'] != hashed_password:
			flash('Invalid Password!')
			return redirect('/')
		else:
			return render_template('success.html')

app.run(debug=True)