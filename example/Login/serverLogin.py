from flask import Flask, request, render_template, redirect, url_for, abort
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('index.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
       user = request.form.get('user', '')
       password = request.form.get('password', '')
                
       if user == 'admin' and password == 'password':
           return redirect(url_for('hello_name',user=user))
       else:
           abort(401)
           
   return render_template('login.html')

if __name__ == '__main__':
  app.run(host='10.20.97.213', port=8080, debug=True)