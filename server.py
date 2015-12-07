#!flask/bin/python
from flask import Flask
from flask import request
from flask import jsonify
from flask import redirect
from flask import url_for
import json
import backend
import logbackend

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://github.com/MARK-III/LogSystem')

@app.route('/body/train', methods=['POST','GET'])
def train():

    if (request.method == 'POST'):
	
    	header = request.headers
    	body = request.get_json(force=True,silent=True)
    	reply = backend.post_train(body)
    	return jsonify(reply)
    else:
	return redirect(url_for('get_records'))

@app.route('/body/records', methods=['GET'])
def get_records():
    return logbackend.body_records.getResponse(request)

if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.0.93',port=10080)
