from app import app, db
from flask import render_template, redirect, url_for, flash
from models import Topic, User
from sqlalchemy import desc
from forms import LoginForm
from flask_login import login_user, current_user, login_required, logout_user


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
    topics_titles = ["<a href='/topic/{}'>{} {}: {}</a>".format(t.id, t.created_on, t.author.username, t.name) for t in
                     topics]
    return '<br>'.join(topics_titles)


@app.route('/topic/<int:id>')
def topic(id):
    topic = Topic.query.get(id)
    topic_messages = ["{} {}: {}".format(m.created_on, m.author.username, m.text) for m in topic.messages]
    return '<br>'.join(topic_messages)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('me'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            form.error = 'Invalid username or password'
            return render_template('login.html', title='Sign In', form=form)
        login_user(user, remember=True)
        return redirect(url_for('me'))

    return render_template('login.html', title='Sign In', form=form)


@app.route('/signup')
def signup():
    return "sign up here"


@app.route('/me')
@login_required
def me():
    return current_user.username


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('topics'))