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
    return render_template('topics.html', topics=topics)


@app.route('/topic/<int:topic_id>')
def topic(topic_id):
    return render_template('messages.html', topic=Topic.query.get(topic_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('topics'))

    form = LoginForm()
    if form.validate_on_submit():
        if not login_user_with_credentials(form.username.data, form.password.data):
            form.error = 'Invalid username or password'
            return render_template('login.html', title='Sign In', form=form)
        return redirect(url_for('topics'))

    return render_template('login.html', title='Sign In', form=form)


@app.route('/signup')
def signup():
    return "Тут будет регистрация."


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('topics'))


def login_user_with_credentials(username, password):
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return False
    login_user(user, remember=True)
    return True


@app.route('/facility_login/<string:username>')
def facility_login(username):
    login_user_with_credentials(username, '123')
    return redirect(url_for('topics'))
