#!/usr/bin/python3

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL

# instanstiate a flask object called app with name of application as first parameter
app = Flask(__name__)
Bootstrap(app)


# app object has a route decorator to handle a request that comes to the end point '/'
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/weight')
def weight():
	return render_template('weight.html')

@app.route('/power')
def power():
	return render_template('power.html')

@app.route('/css')
def css():
	return render_template('css.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
