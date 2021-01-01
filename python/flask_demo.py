from flask import Flask
from flask import request
app = Flask('Flask Demo')
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
     if request.data:
        return 'Got a POST request with a body'
     else:
        return 'Got a POST request without a body'
    else:
     return 'Got a GET request!'


