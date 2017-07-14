from flask import Flask, render_template, session, redirect, flash, request
from mysqlconnection import MySQLConnector
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "Secret"
mysql = MySQLConnector(app,'messages')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=["POST"])
def process():
	if len(request.form['first_name'])<2:
		flash("Fist name cannot be empty")
		return redirect('/')

	elif request.form['first_name'].isalpha() == False:
		flash("Invalid Name")
		return redirect('/')

	if len(request.form['last_name'])<2:
		flash("Last name cannot be empty")
		return redirect('/')

	elif request.form['last_name'].isalpha() == False:
		flash("Invalid Name")
		return redirect('/')

	elif len(request.form['email'])<2:
		flash("Email cannot be empty")
		return redirect('/')

	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid email address!")
		return redirect('/')

	elif len(request.form['password'])<8:
		flash("Password cannot be empty and must be 8 characters")
		return redirect('/')
	else:
		flash('Success!')
		first_name = request.form['first_name']
		last_name = request.form['last_name']
		email = request.form['email']
		password = md5.new(request.form['password']).hexdigest();
		query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"

		data = {
			'first_name': first_name,
			'last_name': last_name,
			'email': email,
			'password': password
		}

		mysql.query_db(query, data)

		return redirect('/wall')

@app.route('/wall')
def wall():
	if 'message' not in session:
		session['message'] = ""

	query = "SELECT * FROM messages"

	get_messages = mysql.query_db(query)

	return render_template('wall.html', messages=session['message'], get_messages = get_messages)

@app.route('/login', methods=["POST"])
def login():
	email = request.form['email']
	password = md5.new(request.form['password']).hexdigest();

	user_query = "SELECT * FROM users WHERE email = :email"
	query_data = {"email": email, "password": password}

	user = mysql.query_db(user_query, query_data)	

	if len(user) != 0:
		hashed_password = md5.new(request.form['password']).hexdigest();
		if user[0]['password'] != hashed_password:
			flash('Invalid Password!')
			return redirect('/')
		else:
			session['id'] = user[0]['id']
			return redirect('/wall')

@app.route('/add_message', methods=["POST"])
def messages():
	query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
	
	message = request.form['message'] 
	session['message'] = message

	data = {
		'message': message,
		'user_id': session['id']
	}

	mysql.query_db(query, data)

	return redirect('/wall')

app.run(debug=True)