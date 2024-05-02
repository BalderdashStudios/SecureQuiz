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
    personalBest = session["BestScore"]
    return render_template('home.html',  personal_Best = personalBest)

@app.route('/startOver')
def startOver():
    session.pop('Q1Selection', None)
    session.pop('Q2Selection', None)
    session.pop('Q3Selection', None)
    #session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1', methods=['GET', 'POST'])
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    if request.method == 'POST':
        if "Q1Selection" in session:
        
            return render_template('page1.html')
        else:
            session["Q1Selection"]=request.form['Q1']
            return render_template('page2.html')
    else:
        error = "Error"
         
    return render_template('home.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    if request.method == 'POST':
        if "Q2Selection" in session:
            
            return render_template('page2.html')
        else:
            session["Q2Selection"]=request.form['Q2']
            return render_template('page3.html')
    else:
         error = "Error"
         
    return render_template('home.html')
    
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    if request.method == 'POST':
        if "Q3Selection" in session:
            return render_template('page3.html')
        else:
            session["Q3Selection"]=request.form['Q3']
        
            Q1Sel = session["Q1Selection"]
            Q2Sel = session["Q2Selection"]
            Q3Sel = session["Q3Selection"]
        
            Answers = ["PhysicallyBasedRendering", "AIUpscaller", "Albedo"]
        
            UserAnswers = [Q1Sel, Q2Sel, Q3Sel]
            
            score = checkAnswers(UserAnswers, Answers)
            
            numberCorrect=(len(score))
            
            session["BestScore"]=numberCorrect
            
            return render_template('End.html', number_correct=numberCorrect)
    else:
         error = "Error"
         
    return render_template('home.html')
    
#Adapted from: https://www.youtube.com/watch?v=oi7IyIrMGMg
def checkAnswers(UA, A):
   correct = []
   for answers in UA:
        if answers in A:
            if answers not in correct:
                correct.append(answers)
   return(correct)
 
    
if __name__=="__main__":
    app.run(debug=True)
