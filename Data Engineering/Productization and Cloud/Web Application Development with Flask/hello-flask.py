from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# set FLASK_APP=hello-flask.py flask run