from flask imort flask

app = Flask(__name__)

@app.route('/')
	def index():
		return render_template("index.html")

@app.route('/process', methods=['POST'])
	def process():
		name = request.form['Your Name']
		return render_template('process.html', name = requst.form['Your Name'])
		


app.rum(debug=True)		