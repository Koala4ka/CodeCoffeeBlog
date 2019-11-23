class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://user:1401@localhost/coffeeproject'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 15
