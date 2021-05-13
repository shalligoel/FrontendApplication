from flask import Flask, redirect, render_template, request, make_response, jsonify, url_for, session
from dblocal import open_connection, insertData
import pymysql
import google.cloud.logging   
from datetime import date



client = google.cloud.logging.Client()  
logger = client.logger('MkGames_logger')  


gameserver = "http://35.202.12.204/index.html"
app = Flask(__name__)
app.secret_key = "super secret key"


conn = open_connection()
@app.route("/", methods=['GET', 'POST'])     ##Endpoints
def main():
    logger.log_struct({'endpoint':'/', 'function':'main', 'page':'index.html'})
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def showsignup():
    logger.log_struct({'endpoint':'/signup', 'function':'showsignup', 'page':'signup.html'})
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    logger.log_struct({'endpoint':'/signin', 'function':'signin', 'page':'signin.html'})
    return render_template('signin.html')

@app.route('/save-signup',methods=['POST', 'GET'])
def signUp():
    if request.method=='POST':
        fname=request.form['fname']
        lname=request.form['lname']
        uname=request.form['uname']
        pwd=request.form['pwd']
        sql = "INSERT INTO Users (firstname,lastname,uname, password) VALUES ('%s', '%s','%s', '%s')"%(fname,lname,uname, pwd)
        print(sql)
        conn = open_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                conn.commit()
        finally:
            conn.close()
        cuser = fname + "  " + lname
        print(cuser)
        response = render_template("game.html", user=cuser)
        #response.set_cookie('YourSessionCookie', cuser)
        session['user'] = cuser # setting session data
        return response 


@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        logger.log_struct({'endpoint':'/login', 'function':'login', 'page':'game.html'})
        uname=request.form['uname']
        pwd=request.form['pwd']
        sql = "select firstname, lastname from Users where uname = '%s'  and password = '%s' limit 1"%(uname,pwd)
        print(sql)
        conn = open_connection()
        try:
            with conn.cursor() as cursor:
                result = cursor.execute(sql)
                if result:
                    row = cursor.fetchone()
                    cuser = row["firstname"] + "  " + row["lastname"]
                    print("User found: %s, opening game"%(cuser))
                    #msg = game-server
                    session['user'] = cuser # setting session data
                    return render_template("game.html",user=cuser)
                else:
                    print("User not found, opening home page")
                    return render_template("index.html")
        finally:
            print("closing connection")
            conn.close()
        


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    logger.log_struct({'endpoint':'/feedback', 'function':'feedback', 'page':'feedback.html'})
    cuser = session['user'] 
    session['user'] = cuser
    return render_template('feedback.html', user=cuser)

@app.route('/save-feedback',methods=['POST', 'GET'])
def savefeedback():
    if request.method=='POST':
        feedback=request.form['feedback']
        cdate = date.today()
        cuser = session['user']
        fname = cuser.split()[0]
        lname = cuser.split()[1]
        print(fname + " " + lname)
        sql = "INSERT INTO Feedbacks (firstname,lastname,feedback, cdate) VALUES ('%s', '%s','%s', '%s')"%(fname,lname,feedback, cdate)
        print(sql)
        conn = open_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                conn.commit()
        finally:
            conn.close()
        result = fname + "  " + lname + " " + feedback
        print(result)
        session['user'] = cuser
        return render_template("response_feedback.html",user=cuser)


@app.route('/score', methods=['GET', 'POST'])
def score():
    logger.log_struct({'endpoint':'/score', 'function':'score', 'page':'score.html'})
    cuser = session['user'] 
    session['user'] = cuser
    return render_template('score.html', user=cuser)

        #return msg #render_template("response_signup.html")
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)








"""
 CREATE TABLE Users (firstname VARCHAR(30) NOT NULL,  lastname VARCHAR(30) NOT NULL, password VARCHAR(20) NOT NULL);



"""
