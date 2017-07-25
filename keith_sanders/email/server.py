from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'email')


@app.route('/')
def index():
    return render_template('index.html')

def val(validation):
    if len(request.form['email']) < 1:
        flash('email not right you fool!')

    else:
        flash('{}.format(request.form[email])) logged!')
    return redirect ('/success')

@app.route('/success', methods=['POST'])
def submit():
    query = "SELECT * FROM email"
    
    email = mysql.query_db(query)

    query = "insert into email (email, created_at, updated_at)values ( :email, NOW(), NOW())"

    data = {
        'email':request.form['email'],
    }
    
    mysql.query_db(query, data)


    return render_template('success.html', email=email)




app.run(debug=True)