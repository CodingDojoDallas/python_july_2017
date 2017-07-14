from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "This Is Secret"

@app.route('/')
def index():
	try:
		session["count"] += 1
	except:
		session["count"] = 0
	print session["count"]
	return render_template("index.html")

@app.route('/add', methods=['POST'])
def add():
	session["count"] += 1
	return redirect('/')

@app.route('/reset_count', methods=['POST'])
def reset():
	session['count'] = 0
	return redirect('/')		

app.run(debug=True)	