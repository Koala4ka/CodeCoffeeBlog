from app import app
from app import db
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    result = db.session.execute('SELECT VERSION()')
    version = [row[0] for row in result][0]
    return render_template('hello.html', mysql_version=version)
