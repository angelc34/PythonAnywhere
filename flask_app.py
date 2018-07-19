# Quickstart on Flask - building my website on python 
# From https://pythonhow.com/how-a-flask-app-works/ 

from flask import Flask, render_template 
# to read the HTML templates and returns it to the webpage 

app = Flask(__name__)
@app.route('/')

# My HOME PAGE 
def home():
    return render_template("homepage.html")

# Link to my ABOUT ME PAGE 
# You could add more pages by adding more Python functions to your script.
@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run( debug = True )

