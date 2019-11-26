from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    topics = db.relationship('Topic', backref='user', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash('123')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @staticmethod
    def login_user_with_credentials(username, password):
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            return False
        login_user(user, remember=True)
        return True


@login.user_loader
def load_user(used_id):
    try:
        return User.query.get(int(used_id))
    except:
        return None


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship("User")
    messages = db.relationship('Message', backref='message_id', lazy=True, order_by="desc(Message.created_on)")
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '<Topic {}>'.format(self.name)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text())
    author = db.relationship("User")
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '<Message {}>'.format(self.text)

