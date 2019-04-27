from flask import Flask, request, render_template, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

@app.route('/')
def main_web():
   return 'main web'

# Cach lay tham so tu requst
@app.route('/hello', methods = ['POST', 'GET'])
def hello_world():
   if request.method == 'POST':
       if 'name' in request.form:
           name = request.form['name']
           return f'Hello {name} from POST method (form-data)'
                        
       elif 'name' in request.json:
           name = request.json['name']
           return f'Hello {name} from POST method (JSON)'        
                        
       else:
           return 'Hello from POST method'
   else:
       name = request.args.get('name', '')
       print(f'Hello {name} from GET method')
       return f'Hello {name} from GET method'


# Mapping tham so tring url
@app.route('/hello/<name>')
def hello_name(name):
  return f'Hello {name}'

@app.route('/student/<int:studentId>')
def getStudent(studentId):
  return f'Student Id = {studentId}'

# su dung template
@app.route('/Usetemplate')
def template():
    return render_template('index.html')

# truyen bien xuong template
@app.route('/VarTemplate/<user>')
def Var_Template(user):
    return render_template('VarTemplate.html', user=user) 

# Redirect and error
@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
       user = request.form.get('user', '')
       password = request.form.get('password', '')
                
       if user == 'nhamtung' and password == '12051994':
           return redirect(url_for('Var_Template',user=user))
       else:
           abort(401)
           
   return render_template('login.html')

# database with flask_sqlalchemy
    # Khai bao model với flask_sqlalchemy
class User(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   userId = db.Column('userId', db.String(20), unique=True)
   userName = db.Column('userName', db.String(50))
   userAge = db.Column('userAge', db.String(10))
  
   def __init__(self, userId, userName, userAge):
       self.userId = userId
       self.userName = userName
       self.userAge = userAge



if __name__ == '__main__':	
   app.run(host='0.0.0.0', port=5000, debug=True)