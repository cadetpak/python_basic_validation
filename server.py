
# pass & passconfirm match

from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "lkjf8lelf"

@app.route('/')
def index(): 
	return render_template("index.html")

@app.route('/process', methods=['POST'])
def process(): 
	if len(request.form['first']) < 1: 
		flash('First Name cannot be empty!','error')
	elif not (request.form['first']).isalpha():  
		flash('First Name cannot contain numbers/special characters!')
	elif len(request.form['last']) < 1: 
		flash('Last Name cannot be empty!', 'error')
	elif not (request.form['last']).isalpha(): 
		flash('Last Name cannot contain numbers/special characters!')
	elif len(request.form['email']) < 1: 
		flash('Email cannot be empty!', 'error')
	elif len(request.form['password']) < 8: 
		flash('Password must be at least 8 characters!', 'error')
	elif len(request.form['password_confirmation']) < 1: 
		flash('Password Confirmation cannot be empty!', 'error')
	elif request.form['password'] != request.form['password_confirmation']: 
		flash('Passwords do not match!', 'error')
	elif not EMAIL_REGEX.match(request.form['email']): 
		flash("Invalid Email Address!")
	else: 
		flash('Successfully registred user!', 'success')
	return redirect('/')

app.run(debug=True)
