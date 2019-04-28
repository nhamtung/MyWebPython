from flask_sqlalchemy import SQLAlchemy
from config import app
import os

db = SQLAlchemy(app)

class Student(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   studentNo = db.Column('student_no', db.String(20), unique=True)
   studentName = db.Column('student_name', db.String(50))
   address = db.Column('address', db.String(50))
  
   def __init__(self, studentNo, studentName, address):
       self.studentNo = studentNo
       self.studentName = studentName
       self.address = address

def getAllStudents():
   return Student.query.all()

def getStudentById(id):
   return Student.query.get(id)

def createStudent(studentNo, studentName, address):
   student = Student(studentNo, studentName, address)
   db.session.add(student)
   db.session.commit()
   return student

def updateStudent(id, studentNo, studentName, address):
   student = Student.query.get(id)
   student.studentNo = studentNo
   student.studentName = studentName
   student.address = address
   db.session.commit()
   return student
       
def deleteStudent(id):
   student = Student.query.get(id)
   db.session.delete(student)
   db.session.commit()

if os.path.isfile('./students.db') == False:
    db.create_all()