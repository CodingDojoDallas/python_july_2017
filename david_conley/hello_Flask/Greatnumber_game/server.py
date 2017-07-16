from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "very secret"

@app.route('/')

def index():
	import random
	session['randnum']=random.randrange(1,101)
	# print session['randnum']
	# print type(session['randnum'])
	return render_template("index.html")

@app.route('/', methods=['GET'])


def results():


app.run(debug=True)	