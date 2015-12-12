#!flask/bin/python
from flask import Flask
from flask import request
from flask import jsonify
from flask import redirect
from flask import url_for
import json
import logbackend

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://github.com/MARK-III/LogSystem')

@app.route('/body/train', methods=['POST'])
def post_train():
    return logbackend.body_train.getResponse(request)

@app.route('/body/records/<date>', methods=['GET'])
def get_records(date):
    return logbackend.body_records.getResponse(request,date)

@app.route('/body/calender/<date>', methods=['GET'])
def get_calender(date):
    return logbackend.body_calender.getResponse(request,date)

@app.route('/body/catalog', methods=['GET'])
def get_catalog():
    return logbackend.body_catalog.getResponse(request)

@app.route('/body/record/<uuid>', methods=['DELETE'])
def delete_record(uuid):
    return logbackend.body_record.getResponse(request,uuid)

if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.0.93',port=10080)
