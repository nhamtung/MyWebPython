from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def hello_world():
   if request.method == 'POST':
       if 'name' in request.form:
           name = request.form['name']
           return 'Hello {} from POST method (form-data)'.format(name)
                        
       elif 'name' in request.json:
           name = request.json['name']
           return 'Hello {} from POST method (JSON)'.format(name)    
                        
       else:
           return 'Hello from POST method'
   else:
       name = request.args.get('name', 'TungNV')
       return "Hello {} from GET method".format(name)

if __name__ == '__main__':
   app.run()
