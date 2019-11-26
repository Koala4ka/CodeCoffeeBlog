class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://user:1401@localhost/coffeeproject'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 15
    SECRET_KEY = '333578AD-58C2-4B19-94F4-A52927EDBD88' # please change this, an output of uuidgen could be used here