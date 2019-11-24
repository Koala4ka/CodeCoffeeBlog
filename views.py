from app import app
from app import db
from flask import render_template
from models import Topic, Message
from sqlalchemy import desc


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    result = db.session.execute('SELECT VERSION()')
    version = [row[0] for row in result][0]
    return render_template('hello.html', mysql_version=version)


@app.route('/topics')
def topics():
    topics = Topic.query.order_by(desc(Topic.created_on)).all()
    topics_titles = ["{} {}: {}".format(t.created_on, t.author.username, t.name) for t in topics]
    return '<br>'.join(topics_titles)


@app.route('/topic/<int:id>')
def topic(id):
    topic = Topic.query.get(id)
    topic_messages = ["{}: {} date of creation {}".format(m.author.username, m.text, m.created_on) for m in topic.messages]
    return '<br>'.join(topic_messages)
