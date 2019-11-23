from models import User
from app import db
from app import bcrypt


def seed():
    if User.query.count() != 0:
        print(User.query.count())
        return None

    user1 = User(username='obama', password_hash=str(bcrypt.generate_password_hash('123')))
    db.session.add(user1)

    user2 = User(username='merkel', password_hash=str(bcrypt.generate_password_hash('123')))
    db.session.add(user2)

    user3 = User(username='elizaveta_ii', password_hash=str(bcrypt.generate_password_hash('123')))
    db.session.add(user3)

    db.session.commit()
