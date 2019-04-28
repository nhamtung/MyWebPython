
from flask import Flask, render_template
from config import app
import db_service
import os

@app.route('/')
def list_student():
    studentList = db_service.getAllStudents()
    if not studentList:
        db_service.createStudent('101', 'Nguyen Van A', 'HaNoi')
        db_service.createStudent('102', 'Nguyễn Văn B', 'Ho Chi Minh')
    return render_template("list_student.html", studentList=studentList)
 
if __name__ == '__main__':
    app.run(debug = True)