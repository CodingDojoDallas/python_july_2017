from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
	return render_template("index.html")

@app.route('/process', methods=['POST'])

def process():
	name = request.form['YourName']
	Dojolocation = request.form['dojolocation']
	FavoriteLanguage = request.form['FavoriteLan']
	return render_template('process.html', 
		name = request.form['YourName'], 
		location = request.form['dojolocation'], 
		language = request.form['FavoriteLan'])
		


app.run(debug=True)		