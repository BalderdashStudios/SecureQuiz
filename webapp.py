import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set on the server. 
                                     #To run locally, set in env.bat (env.sh on Macs) and include that file in gitignore so the secret key is not made public.

@app.route('/', methods=['GET', 'POST'])
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1', methods=['GET', 'POST'])
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    if request.method == 'POST':
        session["Q1Selection"]=request.form['Q1']
        
        print(session["Q1Selection"])
        
        return render_template('page2.html')
    else:
        error = "Error"
         
    return render_template('home.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    if request.method == 'POST':
        session["Q2Selection"]=request.form['Q2']
        
        print(session["Q2Selection"])
        return render_template('page3.html')
    else:
         error = "Error"
         
    return render_template('home.html')
    
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    if request.method == 'POST':
        session["Q3Selection"]=request.form['Q3']
        
        print(session["Q3Selection"])
        return render_template('End.html')
    else:
         error = "Error"
         
    return render_template('home.html')
    
if __name__=="__main__":
    app.run(debug=True)
