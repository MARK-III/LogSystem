#!flask/bin/python
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return ''' How to test api\n
    		   http://[ip address]:10080/test/[some input]'''

@app.route('/test/<input>')
def testapi(input):
	return jsonify(input=input,
				   result='Your data is recorded.')

if __name__ == '__main__':
	app.debug = True
	app.run(host='192.168.0.93',port=10080)
