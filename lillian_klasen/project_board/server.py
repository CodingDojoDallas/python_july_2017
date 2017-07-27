from flask import Flask, render_template, session, redirect, flash, request
from mysqlconnection import MySQLConnector
import re, md5

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "Secret"
mysql = MySQLConnector(app,'projects')

def validate(form_data):
    errors = []

    query = "SELECT * FROM users WHERE email = :email"

    data = {
        'email': form_data['email'],
    }

    user = mysql.query_db(query, data)

    if len(form_data['email']) == 0:
        errors.append("The email cannot be blank.")

    if len(form_data['first_name']) < 2:
        errors.append("First name cannot be blank.")

    if form_data['first_name'].isalpha() == False:
        errors.append("There cannot be numbers in your first name.")

    if form_data['last_name'].isalpha() == False:
        errors.append("There cannot be numbers in your last name.")

    if len(form_data['last_name']) <2:
        errors.append("Last name cannot be blank.")

    if not EMAIL_REGEX.match(form_data['email']):
        errors.append("Please enter a valid email address.")

    if len(form_data['password']) < 8:
        errors.append("Please enter a valid password.")

    if form_data['password'] != form_data['confirm_password']:
        errors.append("Passwords must match")

    if user != []:
        errors.append("Email already in use.")

    return errors


@app.route('/')
def index():
	if 'id' not in session:
		session['id'] = ''
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

    is_valid = validate(request.form)

    if is_valid == []:
        query = "INSERT INTO users (first_name, last_name, email, date_of_birth, password, confirm_password) VALUES (:first_name, :last_name, :email, :date_of_birth, :password, :confirm_password)"

        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'date_of_birth': request.form['dob'],
            'email': request.form['email'],
            'password': md5.new(request.form['password']).hexdigest(),
            'confirm_password': md5.new(request.form['confirm_password']).hexdigest()
            }

        user_id = mysql.query_db(query, data)
        session['user_id'] = user_id

        return redirect('/dashboard')

    else:
        for error in is_valid:
            flash(error)
        return redirect('/')

@app.route('/login', methods=["post"])
def login():
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    projects = mysql.query_db('SELECT projects.project_name, projects.due_date FROM projects')
    return render_template('dashboard.html', projects=projects)

@app.route('/add_project', methods=['post'])
def add_project():
    return render_template('add.html')

@app.route('/add', methods=['post'])
def add():
    query = "SELECT id FROM users where id = :id"

    data = {
        'id': session['user_id']
    }

    user_id = mysql.query_db(query, data)

    query = "INSERT INTO projects (project_name, due_date, description, created_at, updated_at, user_id) VALUES (:project_name, :due_date, :description, NOW(), NOW(), :user_id)"

    data = {
        'project_name': request.form['name'],
        'due_date': request.form['deadline'],
        'description': request.form['description'],
        'user_id': session['user_id']
    }

    mysql.query_db(query, data)

    return redirect('/dashboard')

app.run(debug=True)
