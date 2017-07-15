from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'Key'

@app.route('/')
def sessionCounter():
    try:
        session['counter']+=1
    except KeyError:
        session['counter'] = 1
    return render_template('index1.html', counter=session['counter'])

@app.route('/addtwo', methods=['GET','POST'])
def buttonAddTwo():
    session['counter']+=2
    return render_template('index1.html', counter=session['counter'])
    return redirect('/')

@app.route('/reset', methods=['GET','POST'])
def buttonReset():
    session.clear()
    return redirect('/')

app.run(debug=True)
