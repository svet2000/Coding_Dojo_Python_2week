from flask import Flask, render_template, redirect, request, session, flash
import re # the "re" module will let us perform some regular expression operations
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')# create a regular expression object that we can use run operations
app = Flask(__name__)
app.secret_key = "Key"

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    email=request.form['email']
    password=request.form['password']
    confirm=request.form['confirm_password']

    if len(email) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(email):
        flash("Invalid Email Address!")
    else:
        flash("Success!")

    if len(password)<=8:
        flash("Password cannot be less than 8!")
    else:
        if password!=confirm_password:
            flash("Confirm your password!")
        else:
            flash("Success!")

    if str.isalpha(first_name)==False or str.isalpha(last_name)==False:
        flash("First name and last name can not contain numbers")
    elif first_name<1 or last_name<1:
        flash("First name and last name cannot be blank!")
    else:
        flash("Success!")
    return redirect('/')

app.run(debug=True)
