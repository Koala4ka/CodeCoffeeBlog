from models import User, Topic, Message
from app import db
from app import bcrypt
from datetime import datetime, timedelta


def time_ago(delta):
    return datetime.now() - timedelta(hours=delta,
                                      minutes=delta,
                                      seconds=delta)

def seed_users():
    users_count = User.query.count()
    print(f'Users count: {users_count}')

    if users_count != 0:
        return None

    user1 = User(username='obama', password_hash=str(bcrypt.generate_password_hash('123')))
    db.session.add(user1)

    user2 = User(username='merkel', password_hash=str(bcrypt.generate_password_hash('123')))
    db.session.add(user2)

    user3 = User(username='elizaveta_ii', password_hash=str(bcrypt.generate_password_hash('123')))
    db.session.add(user3)

    db.session.commit()


def seed_topics():
    topics_count = Topic.query.count()
    print(f'Topics count: {topics_count}')

    if topics_count != 0:
        return None

    user1 = User.query.filter_by(username='obama').first()
    user2 = User.query.filter_by(username='merkel').first()
    user3 = User.query.filter_by(username='elizaveta_ii').first()
    assert(user1 is not None and user2 is not None and user3 is not None)

    topic1 = Topic(name='Beer or wine', author_id=user1.id, created_on=time_ago(1), updated_on=time_ago(1))
    db.session.add(topic1)

    topic2 = Topic(name='iOS or Android', author_id=user2.id, created_on=time_ago(2), updated_on=time_ago(2))
    db.session.add(topic2)

    topic3 = Topic(name='Meat or fish', author_id=user3.id, created_on=time_ago(3), updated_on=time_ago(3))
    db.session.add(topic3)

    topic4 = Topic(name='Hen or egg', author_id=user1.id, created_on=time_ago(4), updated_on=time_ago(4))
    db.session.add(topic4)

    db.session.commit()
