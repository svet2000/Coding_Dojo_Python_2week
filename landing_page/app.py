from flask import Flask, render_template, redirect, request
app = Flask (__name__)
@app.route('/')
def funcHello():
    return render_template('html.html',name = "Svetlana", phrase = "hello", times = 5)
@app.route('/ninjas')
def Ninjafunc():
    return render_template('ninja.html')

@app.route('/dojos/new', methods=['POST'])
def DojosFunc():
    return render_template('dojos.html')

app.run(debug=True)



#Example from Flask documentation
#@app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         do_the_login()
#     else:
#         show_the_login_form()
