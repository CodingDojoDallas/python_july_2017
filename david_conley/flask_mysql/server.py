from flask import Flask
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
@app.route('/')
def index()
    print "Inside the index method."
# an example of running a query
print mysql.query_db("SELECT * FROM users")

retrun render_template('index.html')

app.run(debug=True)
