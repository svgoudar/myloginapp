from flask import Flask, render_template, request, redirect, url_for, session, flash
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
# from pymysql import cursors
import psycopg2
from datetime import datetime

import re
import base64
import db
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = '1a2b3c4d5eABCDE'
# MySQL configurations
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
# app.config['SECRET_KEY'] = 'SVGmaster483'
# app.config['MYSQL_DATABASE_DB'] = 'ACCOUNT_DB'
# app.config['MYSQL_DATABASE_HOST'] = 'my-db.cqqwf49htgq1.us-east-2.rds.amazonaws.com'
# mysql = MySQ
# mysql.init_app(app)

# db.DB_CONF()

connection = psycopg2.connect(user="sxflbeuumpoxid",
                              password="a92972339779fd8a058b5558540df78185203310faa8a05bf6031bef4a07430f",
                              host="ec2-35-172-246-19.compute-1.amazonaws.com",
                              port="5432",
                              database="da8mke9e8qna4a")


# db = SQLAlchemy(app)
# migrate = Migrate(app,db)
cur = connection.cursor()
# cur.execute("SELECT * FROM ACCOUNTS;")


# Intialize MySQL

def encode_password(stringpass):
    strbytes =stringpass.encode('ascii')
    strbcode =base64.b64encode(strbytes)
    return strbcode.decode('ascii')

@app.route("/")
@app.route('/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
	# return render_template('home.html', username=session['username'])
        return render_template('home.html')
#         return render_template('home.html', username=session['username'])
    else:
        return render_template('home.html')
    # User is not loggedin redirect to login page
    # return redirect(url_for('login'))


# http://localhost:5000/pythonlogin/ - this will be the login page, we need to use both GET and POST requests
@app.route('/login', methods=['GET', 'POST'])
def login():
# Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # print(password)
        # Check if account exists using MySQL
        print(username,password)
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(f'''SELECT * FROM ACCOUNTS WHERE USERNAME = '{str(username)}' AND PASSWORD = '{password}';''')
        # Fetch one record and return result
        account = cur.fetchone()
        print(account)
                # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
#             session['id'] = account['USER_ID']
#             session['username'] = account['USERNAME']
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg=msg)


# http://localhost:5000/pythinlogin/register - this will be the registration page, we need to use both GET and POST requests
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
                # Check if account exists using MySQL
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('''SELECT * FROM ACCOUNTS WHERE USERNAME = '%s';'''%(username))
        account = cur.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
	    now = datetime.now()
#             dtime=datetime.now()
	    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
	%m/%d/%Y, %H:%M:%S"
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cur.execute('''INSERT INTO ACCOUNTS(USERNAME,PASSWORD,EMAIL,CREATED_ON) VALUES ( '%s', '%s', '%s','%d');'''%(username,password,email,date_time))
            cur.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)

# http://localhost:5000/pythinlogin/home - this will be the home page, only accessible for loggedin users


# @app.route("/register")
# @app.route("/register",methods=['GET','POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f"Account created for {form.username.data}!",'success')
#         return redirect(url_for('home'))
#     return  render_template('register.html',title='Register',form=form)
@app.route("/logout")
def logout():
   # remove the username from the session if it is there
   # session.pop('username',None)
   return redirect(url_for('home'))




if __name__ =='__main__':
    # app.run(debug=)
	app.run(debug=True)







