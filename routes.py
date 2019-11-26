from app import app, db
from flask import render_template, redirect, url_for
from models import Topic, User
from sqlalchemy import desc
from forms import LoginForm, SignupForm
from flask_login import login_user, current_user, logout_user


@app.route('/rebuildall')
def index():
    return render_template('rebuildall.html')


@app.route('/hello')
def hello():
    result = db.session.execute('SELECT VERSION()')
    version = [row[0] for row in result][0]
    return render_template('hello.html', mysql_version=version)


@app.route('/')
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
        if User.login_user_with_credentials(form.username.data, form.password.data):
            return redirect(url_for('topics'))
        else:
            form.password.errors.append('Неправильный логин или пароль')
            return render_template('login.html', form=form)

    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('/'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        return redirect(url_for('topics'))
    return render_template('signup.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('topics'))


@app.route('/facility_login/<string:username>')
def facility_login(username):
    User.login_user_with_credentials(username, '123')
    return redirect(url_for('topics'))
