from flask import Flask, render_template, request, redirect, flash
app=Flask(__name__)
app.secret_key='key'

@app.route('/', methods=['GET','POST'])
def func():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def funcResult():
    name = request.form['name']
    if len(name)<1:
        flash('Name field can not be empty')
    else:
        flash('Your name is {}'.name)
    location = request.form['locations']
    language = request.form['languages']
    comment = request.form['comment']
    if len(name)<1:
        flash('Comment field can not be empty')
    elif len(name)>120:
        flash('Comment field can not be longer than 120')
    else:
        flash('Your comment is {}'.comment)
    return render_template('index1.html',name=name,location=location,language=language,comment=comment)
    return redirect('/')
app.run(debug=True)


# @app.route('/process', methods=['POST'])
# def process():
#   if len(request.form['name']) < 1:
#     # display validation errors
#   else:
#     # display success message
#   return redirect('/') # either way the application should return to the index and display the message
