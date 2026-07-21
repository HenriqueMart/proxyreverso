import os
from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app):
    app.config['MYSQL_HOST'] = os.getenv('DB_HOST', 'banco')
    
    app.config['MYSQL_USER'] = os.getenv('DB_USER', 'root')
    app.config['MYSQL_PASSWORD'] = os.getenv('DB_PASSWORD', '123')
    app.config['MYSQL_DB'] = os.getenv('DB_NAME', 'app_db')
    
    mysql.init_app(app)