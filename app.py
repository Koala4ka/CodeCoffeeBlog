from flask import Flask
from config import Configuration
import pymysql

app = Flask(__name__)
app.config.from_object(Configuration)
db = pymysql.connect(host=app.config["DB_HOST"], 
					user=app.config["DB_USER"], 
					password=app.config["DB_PASSWORD"], 
					database=app.config["DB_DATABASE"])

if __name__ == '__main__':
    app.run()
