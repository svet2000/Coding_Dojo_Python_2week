from flask import Flask, render_template, request, redirect
app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def func():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def funcResult():
    name = request.form['name']
    location = request.form['locations']
    language = request.form['languages']
    comment = request.form['comment']
    return render_template('index1.html',name=name,location=location,language=language,comment=comment)
    return redirect('/')
app.run(debug=True)
