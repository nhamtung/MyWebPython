from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
  return 'Hello {}'.format(name)

@app.route('/student/<int:studentId>')
def getStudent(studentId):
  return 'Student {}'.format(studentId)
 
if __name__ == '__main__':
  app.run(debug = True)