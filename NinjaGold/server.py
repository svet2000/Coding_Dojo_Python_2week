from flask import Flask, render_template, redirect, session, request
import random, datetime
from datetime import datetime
app = Flask(__name__)
app.secret_key = "Secret"

# session.pop('gold',None)
# session.pop('activity',None)

@app.route('/')
def index():
    session.clear()
    if 'gold' not in session: #if we just started playing
        session['activity']=[]
        session['gold']=0
    return render_template ('index.html')

@app.route('/process_money', methods=['POST'])
def processMoney():
    if request.form['action']=='farm':
        earned=random.randrange(10,21)
        session['gold']+=earned
        message = "Earned"+" "+str(earned)+" "+"gold from the farm"+" "+str(datetime.now().strftime("%Y/%m/%d %I:%M %p"))
        try:
            session['activity'] += message + '\n'
        except KeyError:
            session['activity'] = message + '\n'
        print earned,'farm'
    elif request.form['action']=='cave':
        earned=random.randrange(5,11)
        session['gold']+=earned
        message = "Earned"+" "+str(earned)+" "+"gold from the cave"+" "+str(datetime.now().strftime("%Y/%m/%d %I:%M %p"))
        try:
            session['activity'] += message + '\n'
        except KeyError:
            session['activity'] = message + '\n'
        print earned, "cave"
    elif request.form['action']=='house':
        earned=random.randrange(2,6)
        session['gold']+=earned
        message = "Earned"+" "+str(earned)+" "+"gold from the house"+" "+str(datetime.now().strftime("%Y/%m/%d %I:%M %p"))
        try:
            session['activity'] += message + '\n'
        except KeyError:
            session['activity'] = message + '\n'
        print earned,"house"
    elif request.form['action']=='casino':
        earned=random.randrange(-50,51)
        session['gold']+=earned
        if earned>0:
            message = "Earned"+" "+str(earned)+" "+"gold from the casino"+" "+str(datetime.now().strftime("%Y/%m/%d %I:%M %p"))
        elif earned<=0:
            message = "Lost"+" "+str(earned)+" "+"gold from the casino"+" "+str(datetime.now().strftime("%Y/%m/%d %I:%M %p"))
        try:
            session['activity'] += message + '\n'
        except KeyError:
            session['activity'] = message + '\n'
        print earned, "casino"
    print session['gold'],'SUM'
    return redirect ('/')
app.run(debug=True)
