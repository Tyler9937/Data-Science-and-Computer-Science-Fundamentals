from flask import Flask
from model import clf
from model import X_test, y_test

# set FLASK_APP=app.py flask run

app = Flask(__name__)

@app.route("/")
def landing_page():
    return 'Welcome to iris predictor. use /score, /predict, /iris to anaylis iris model with flask webapp'

@app.route('/score')
def score():
    '''Scores the accuracy of the regression'''
    return str(clf.score(X_test, y_test))

@app.route('/predict')
def predict():
    '''Predicts the y values of the test data'''
    return str(clf.predict(X_test))

@app.route('/iris')
def iris():
    '''Displays the data within X_test'''
    return str(X_test)
