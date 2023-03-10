#!/usr/bin/python3

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL

# instanstiate a flask object called app with name of application as first parameter
app = Flask(__name__)
Bootstrap(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1


# app object has a route decorator to handle a request that comes to the end point '/'
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/runstats')
def runstats():
	return render_template('runstats.html')

@app.route('/weight')
def weight():
	return render_template('weight.html')

@app.route('/power')
def power():
	return render_template('power.html')

@app.route('/recovery')
def recovery():
	return render_template('recovery.html')

@app.route('/regression')
def regression():
	return render_template('regression.html')

@app.route('/scatter')
def scatter():
	return render_template('scatter.html')

# No caching at all for API endpoints.
@app.after_request
def add_header(response):
	# response.cache_control.no_store = True
	response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
	response.headers['Pragma'] = 'no-cache'
	response.headers['Expires'] = '-1'
	return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
