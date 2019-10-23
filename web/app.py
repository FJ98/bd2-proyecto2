from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, session, Response
import json


from datetime import datetime


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rankedRetrieval')
def rankedRetrieval():
    return render_template('ranked.html')

@app.route('/do_ranked_search', methods=['POST','GET'])
def do_login():
    query = request.form['query']


    for user in users:
        if user.username == username and user.password == password:
            session['username'] = username
            session['password'] = password
            return render_template("name_sala.html")

    return render_template("fail.html")





if __name__ == '__main__':
    app.run(debug=True)
