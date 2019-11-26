from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

import seed

@app.cli.command("seed_db")
def seed_db():
    seed.seed_users()
    seed.seed_topics()
    seed.seed_messages()


if __name__ == '__main__':
    app.run()
