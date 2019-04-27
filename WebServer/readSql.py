from server import db, User
import os

def createDb():
  if os.path.isfile('./users.db') == False:
    db.create_all()
    addUser('123', 'nhamtung', '18')
    addUser('125', 'TungNV', '19')

def addUser(userId, userName, userAge):
  user = User(userId, userName, userAge)
  db.session.add(user)
  db.session.commit()

def editUser(id, userId, userName, userAge):
  user = User.query.get(id)
  user.userId = userId
  user.userName = userName
  user.userAge = userAge
  db.session.commit()
  readUser(id)

def deleteUser(id):
  user = User.query.get(id)
  db.session.delete(user)
  b.session.commit()

def readUser(id):
  user = User.query.get(id)
  print(f'userID: {user.userId}, userName: {user.userName}, userAge: {user.userAge}')

def readAllUser():
  users = User.query.all()
  for user in users:
    print(f'userID: {user.userId}, userName: {user.userName}, userAge: {user.userAge}')

createDb()
readAllUser()
editUser(2, '124', 'NhanPT', '17')