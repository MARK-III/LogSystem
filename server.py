#!flask/bin/python
from flask import Flask
from flask import request
from flask import jsonify
import json
import backend

app = Flask(__name__)

@app.route('/')
def index():
    return ''' Refer to https://github.com/MARK-III/LogSystem'''

@app.route('/body/train', methods=['POST','GET'])
def train():
    if request.method == 'POST':
        content = request.get_json(force=True,silent=True)
        backend.post_train(content)
	return jsonify(content) 
    else:
        return jsonify(status="recorded",
		       name="Dead lift",
                       weight=30,
                       created_at="2015-11-27T00:12:55Z")

if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.0.93',port=10080)
