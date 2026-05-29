from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'apiuser'
    app.config['MYSQL_PASSWORD'] = '123'
    app.config['MYSQL_DB'] = 'minha_api'
    mysql.init_app(app)
