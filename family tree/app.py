# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def me():

    name = "name1" # write your name
    age = "18" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/")
def father():

    name = "name2" # write your name
    age = "56" # write your age

    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/")
def mother():

    name = "name3" # write your name
    age = "50" # write your age

    return render_template('mother.html' , name = name , age = age)


# define the route to friends webpage
@app.route("/")
def friend():

    name = "name4" # write your name
    age = "18" # write your age

    return render_template('friend.html' , name = name , age = age)


# add other routes, if you want


# run the file
app.run(debug=True)