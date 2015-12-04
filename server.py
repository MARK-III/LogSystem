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

    if (request.method == 'POST'):
	
    	header = request.headers
    	body = request.post_body_json(force=True,silent=True)
    	reply = backend.post_train(header='',body)
    	return jsonify(reply)
    else:
	header = request.headers
	reply = backend.get_body__train(header='')
	return jsonify(reply)

if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.0.93',port=10080)
