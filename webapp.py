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

@app.route('/' methods=['GET', 'POST'])
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1' methods=['GET', 'POST'])
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    session["firstName"]=request.form['firstName']
    session["lastName"]=request.form['lastName']
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    session["favoriteColor"]=request.form['favoriteColor']
    return render_template('page3.html')
    
if __name__=="__main__":
    app.run(debug=False)


#TO BE ADAPTED
if request.method == 'POST':
        color = request.form['color'] 
        n = int(request.form['multNum']) #values in request.args are strings by default
        reply2 = "2 x " + str(n) + " = " + str((2*n))
        if color == 'pink':
            reply1 = "That's my favorite color, too!"
            return render_template('response.html', response1 = reply1, response2 = reply2)
        else:
            reply1 = "My favorite color is pink."
            return render_template('response.html', response1 = reply1, response2 = reply2)
    else:
        reply1 = "Error"
         
    return render_template('home.html')