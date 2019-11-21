from app import app
from app import db
from flask import current_app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    if db.open is False: db.ping(reconnect=True)
    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    cur.close()
    return render_template('hello.html', mysql_version=cur.fetchone()[0])