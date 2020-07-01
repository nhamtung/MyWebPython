from flask import Flask, jsonify, request, render_template, redirect, url_for, abort
from flask_jwt import JWT, jwt_required, current_identity

class User(object):
   def __init__(self, id, username, password):
       self.id = id
       self.username = username
       self.password = password

users = [
   User(1, "admin", "abc@123"),
   User(2, "guest", "1234"),
]

username_table = {u.username: u for u in users}
userid_table = {u.id : u for u in users}

def authenticate(username, password):
  user = username_table.get(username, None)
  if user and user.password == password:
    return user

def identity(payload):
   userid = payload['identity']
   return userid_table[userid]

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'abcdxyztuv'

jwt = JWT(app, authenticate, identity)

@app.route('/list_student')
@jwt_required()
def list_student_api():
   studentList = [
       {'id' : 1, 'name' : 'Nguyễn Văn An'},
       {'id' : 2, 'name' : 'Nguyễn Thị Binh'},        
   ]
   return jsonify({'username' : current_identity.username, 'students' : studentList})

if __name__ == '__main__':
   app.run()