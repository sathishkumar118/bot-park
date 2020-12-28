# app.py
from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    app.debug = False                   # run the flask app
    port = int(os.environ.get('PORT', 33507))
    waitress.serve(app, port=port)
