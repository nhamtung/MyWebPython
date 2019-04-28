from flask import Flask, render_template
from config import app
import db_service

@app.router('/')
def list_student():
    if os.path.exit() == False:
        db_service.createStudent('101', 'Nguyen Van A', 'HaNoi')
        db_service.createStudent('102', 'Nguyễn Văn B', 'Ho Chi Minh')

    studentList = db_service.getAllStudents()
    return render_template('list_student.html', studentList = studentList)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '5000', debug = True)