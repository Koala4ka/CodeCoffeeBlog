from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Configuration
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# ----

from models import User
bcrypt = Bcrypt(app)

# ----

import click
import seed

@app.cli.command("seed_db")
def seed_db():
    seed.seed()
    
# ----

if __name__ == '__main__':
    app.run()
