from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('hello_flask.html', name='Kevin')

app.run(debug=True)
