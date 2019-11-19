from app import app
from app import db
from flask import current_app
from flask import render_template

@app.route('/')
def index():
    return ""

@app.route('/hello')
def hello():
    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    return render_template('hello.html', mysql_version=cur.fetchone()[0])