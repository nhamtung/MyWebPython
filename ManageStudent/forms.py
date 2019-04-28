import os
import db_service
from config import app

class StudentForm():
	def __init__(self, request=None, dbModel=None):
		if request:
			self.studentId = request.form['studentId']
			self.studentNo = request.form['studentNo']
			self.studentName = request.form['studentName']
			self.address = request.form['address']

			file = request.files.get('profilePicture')
			if file and file.filename != '':
				self.profilePictureFile = file
			else:
				self.profilePictureFile = None
		elif dbModel:
			self.studentId = dbModel.Id
			self.studentNo = dbModel.studentNo
			self.studentName = dbModel.studentName
			self.address = dbModel.address

	def validate(self):
		errorList = []
		if not self.studentNo:
			errorList.append('Student Number is required')
		if not self.studentName:
			errorList.append('Student Name is required')
		if not self.address:
			errorList.append('Address is required')
		if not self.studentId and not self.profilePictureFile:
			errorList.append('Profile picture is required')
		return errorList

	def save(self):
		if self.studentId:
			student = db_service.updateStudent(self.studentId, self.studentNo, self.studentName, self.address)
		else:
			student = db_service.createStudent(self.studentId, self.studentNo, self.studentName, self.address)

		if student and self.profilePictureFile:
			self.profilePictureFile.save(os.path.join(app.config['IMG_DIR'], str(studentId) + '.jpg'))

