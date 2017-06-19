from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['POST', "GET"])
def index():
    return render_template('index.html')


@app.route('/validate-signup', methods=['POST'])
def validate_signup():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

#for username needs to have >3, <8 chars no spaces | field can stay (GET)
    
    if len(username) > 8 or len(username) < 3 or not username.isalpha():
        username_error = 'Thats not a valid username'

#for password needs to have >3, <8 chars no spaces, different from username | field needs to be cleared (POST)
    if not password.isalpha():
        password_error = 'That\'s not a valid password'
        password = ''
    elif password == username:
        password_error = 'You can not use the same username and password'
        password = ''
    else:
        password = str(password)
        if len(password) > 8 or len(password) < 3:
            password_error = 'Password must have more than 3 and less than 8 characters'
            password = ''
#for verify password needs to match password | field needs to be cleared (POST)
    if password != verify:
        verify_error = 'Passwords don\'t match'
        verify = ''
    
#for email (if provided) needs to be valid email - it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long | field can stay (GET)
    if email:
        if '@' not in email or '.' not in email:
            email_error = 'That\'s not a valid email'


    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username) #passing the template directly into if statement
    else: 
        return render_template('/index.html', username_error=username_error, password_error=password_error, email_error=email_error, username=username, password=password, email=email, verify=verify, verify_error=verify_error)


    #username = request.form['username']

app.run()
