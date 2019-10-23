from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, request, url_for
import flask_whooshalchemy as wa
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['WHOOSH_TABLE'] = 'whoosh'

db = SQLAlchemy(app)


class Post(db.Model):
    __searchable__ = ['title', 'content']
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(1000))
    #completed = db.Column(db.Integer, default=0)
    #date_created = db.Column(db.DateTime, default=datetime.utcnow())

    #def __repr__(self):
    #    return '<Task %r>' % self.id


# wa.whoosh_index(app, Post)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        post = Post(title=request.form['title'], content=request.form['content'])
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)
