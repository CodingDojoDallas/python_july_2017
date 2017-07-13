from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/web_page')
def web_page():
	return render_template("web_page.html")

@app.route('/about_me')
def about_me():
	return render_template("about_me.html")

app.run(debug=True) 
