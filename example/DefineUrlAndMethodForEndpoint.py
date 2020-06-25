from flask import Flask, request
app = Flask(__name__)

@app.route('/hello', methods = ['POST', 'GET'])
def hello_world():
   if request.method == 'POST':
       return 'Hello from POST method'
   else:
       return 'Hello from GET method'

if __name__ == '__main__':
   app.run()