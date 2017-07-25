from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'Key'

@app.route('/', methods=['GET','POST'])
def func():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def funcResult():
    session['name'] = request.form['name']
    session['location'] = request.form['locations']
    session['language'] = request.form['languages']
    session['comment'] = request.form['comment']
    return render_template('index1.html',name=session['name'],location=session['location'],language=session['language'],comment=session['comment'])
    return redirect('/')
app.run(debug=True)
