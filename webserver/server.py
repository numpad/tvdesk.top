from flask import *
import random
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
	url_for('static', filename="style.css")
	return render_template("index.html")

@app.route('/about')
def about():
	url_for('static', filename="style.css")
	return render_template("about.html")

@app.route('/layout', methods=['GET', 'POST'])
def layout():
	url_for('static', filename="style.css")
	if request.method == 'POST':
		return render_template("layout.html", videos=request.values)
	else:
		return "please submit your videos first"

@app.route('/process', methods=['POST'])
def process():
	url_for('static', filename="style.css")
	urls = [request.values[url] if url.startswith('url') else None for url in request.values]
	return render_template("processing.html", urls=urls, accesscode=randomCode(urls))

@app.route('/process/<code>', methods=['GET'])
def process_get(code):
	url_for('static', filename="style.css")
	return render_template("waiting.html", accesscode=code, percentdone="92")


def randomCode(urls):
	bigurlstring = "".join(urls)
	return str(hashlib.sha256(bigurlstring.encode('utf-8')).hexdigest())[:6]
