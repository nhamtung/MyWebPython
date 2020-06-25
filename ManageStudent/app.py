
from flask import Flask, render_template, request, redirect, url_for, jsonify
import traceback
import time

from forms import StudentForm
from config import app
import db_service
import os

@app.route('/student/add_edit/<int:studentId>', methods = ['GET', 'POST'])
def add_edit_student(studentId):
	errorList = []
	form = StudentForm()

	if request.method == 'POST':
		try:
			form = StudentForm(request)
			errorList = form.validate()
			if not errorList:
				student = form.save()
				return redirect(url_for('list_student'))
		except Exception as e:
			traceback.print_exc()
			errorList.append(str(e))
	elif studentId>0:
		student = db_service.getStudentById(studentId)
		form = StudentForm(dbModel=student)
	return render_template('add_edit_student.html', form=form, errorList=errorList)

@app.route('/student/delete/<int:studentId>')
def delete_student(studentId):
	try:
		db_service.deleteStudent(studentId)
	except Exception as e:
		traceback.print_exc()
	return redirect(url_for('list_student'))	

@app.route('/')
def list_student():
    studentList = db_service.getAllStudents()
    if not studentList:
        db_service.createStudent('101', 'Nguyen Van A', 'HaNoi')
        db_service.createStudent('102', 'Nguyễn Văn B', 'Ho Chi Minh')
    return render_template("list_student.html", studentList=studentList)
 
if __name__ == '__main__':
    app.run(host='10.20.97.213', port=8080, debug = True)