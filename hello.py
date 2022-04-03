from flask import Flask


app = Flask(__name__)

@app.route("/")

def hello_world():
    return "Hello, world! :yeet:"


# in the command line then we enter:
# > export FLASK_APP=hello.py
# > flask run

# app can then be accessed from