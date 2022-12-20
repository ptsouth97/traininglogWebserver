#!/usr/bin/python3

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
#import yaml

# instanstiate a flask object called app with name of application as first parameter
app = Flask(__name__)
Bootstrap(app)

# Configure db
#db = yaml.load(open('db.yaml'))
#app.config['MYSQL_HOST'] = db['mysql_host']
#app.config['MYSQL_USER'] = db['mysql_user']
#app.config['MYSQL_PASSWORD'] = db['mysql_password']
#app.config['MYSQL_DB'] = db['mysql_db']
#mysql = MySQL(app)

# app object has a route decorator to handle a request that comes to the end point '/'
@app.route('/')
def index():
	#fruits = ['Apple', 'Mango', 'Orange']

	
	return render_template('index.html') #, fruits=fruits)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/css')
def css():
	return render_template('css.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
