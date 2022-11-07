# Team Mykolyk Fan Club: Shafiul Haque, David Deng, April Li
# SoftDev pd08
# K19: Sessions Greetings
# 2022-11-04
# time spent: 0.3hrs

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

mydict = {}

app.secret_key = 'hi'
username = 'bruh'
password = 'bruh2'

def filereader():
    file1 = open("devofam.csv",'r')
    sha = file1.readlines()
    for e in sha:
        ar = e.split(',')
        ar[2] = ar[2][0:len(ar[2])-1]
        mydict[ar[0]] = ar[2]
filereader()


@app.route('/')
def show():
    if 'username' in session: #if user is already in session, will go to response page logged in
        return render_template('response.html', username = session['username'])
    return render_template('login.html') #if user isn't already logged in go to login page

@app.route("/login", methods=['GET', 'POST'])
def disp_loginpage():
    if request.method == 'POST' and request.form['username'] == username:
        print(request.form['username'])
        print(request.form['password'])
        if request.form['password'] == password:
            print(session)
            session['username'] = request.form['username']
            return render_template('response.html', username = session['username'])
        return render_template('login.html', error="incorrect password") #in case the password is incorrect
    return render_template('login.html', error ="incorrect username") #in case the username is incorrect


@app.route("/logout", methods=['GET', 'POST'])
def disp_logoutpage():
    session.pop('username')
    return render_template('login.html')


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
