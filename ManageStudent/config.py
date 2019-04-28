from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:1234@localhost/testdb'
app.config['IMG_DIR'] = 'static/images'
app.config['SECRET_KEY'] = '12051994'