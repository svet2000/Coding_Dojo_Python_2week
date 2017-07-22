from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = 'Key'

random_number= random.randrange(0, 101)#random number to compare with
@app.route('/')
def index():
    session ['someKey']= random_number
    print session ['someKey'],"**"
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
    session['message']=0
    number_input=request.form['number_input']#number which was printed in a form
    print number_input,"*"
    if int(number_input)>session['someKey']:
        session['message']='Higher'
        print session['message']

    elif int(number_input)<session['someKey']:
        session['message']='Lower'
        print session['message']

    else:
        session['message']='Winner'
        print session['message']
    return redirect('/')

@app.route('/winner')
def winner():
    session.pop('someKey')  #clean the session dictionary
    session.pop('message')
    return redirect('/')

app.run(debug=True)
