#Importing flask module in the project
from flask import Flask, render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
# @app.route("/flask_1")

#run the application on local server
# app.run()

@app.route("/")

def second_flask():
    name = 'Nash'
    return render_template('template/index.html', index_variable = name)

app.run(debug=True)