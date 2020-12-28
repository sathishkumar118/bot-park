# app.py
from flask import Flask           # import flask
my_awesome_app = Flask(__name__)             # create an app instance

@my_awesome_app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    my_awesome_app.run()                     # run the flask app
