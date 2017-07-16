from flask import Flask, request, render_template, redirect, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'world')

@app.route('/')
def index():
    print "Inside the index method."

    query = "insert into languages (country_code, language, is_official, percentage, country_id) values (:country_code, :language, :is_official, :percentage, :country_id)"
    data = {
        'country_code': 'USA',
        'language': 'Klingon',
        'is_official': True,
        'percentage': '2',
        'country_id': 224,
    }

    id = mysql.query_db(query, data)

    print id

    return render_template('index.html')

app.run(debug=True)