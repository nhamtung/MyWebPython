
from flask import Flask

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:12051994@127.0.0.1/db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['IMG_DIR'] = 'static/images'
app.config['SECRET_KEY'] = "abcxyztuv"