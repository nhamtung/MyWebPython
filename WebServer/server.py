
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def main_web():
   return 'main web'

@app.route('/hello', methods = ['POST', 'GET'])
def hello_world():
   if request.method == 'POST':
       return 'Hello from POST method'
   else:
       return 'Hello from GET method'

@app.route('/TungNV')
def MyName():
   return 'I am TungNV' 

if __name__ == '__main__':	
   app.run(host='0.0.0.0', port=5000, debug=True)