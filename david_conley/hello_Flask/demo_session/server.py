from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = "ThisIsSecret"


@app.route('/')
def index():
	if'number' not in session:
		session['counter'] = 0

	session['number'] += 1	

	return reder_template('index.html', couner=session['number'])	

def process():




app.run(debug=True)
