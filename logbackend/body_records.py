import json
import sqlite3
from datetime import datetime
from flask import request
from flask import jsonify
from flask import json

def getResponse(request,date):
   
    connection = sqlite3.connect('/home/linaro/LogSystem/test.db')
    cur = connection.cursor()
    result = cur.execute("SELECT exercise_id,catalog_id,resistance,repetition,date,record_id from main where date = '%s'" % date)
    records_list = []
    for row in result:

	record_dict = {
		       'exercise': row[0],
		       'catalog': row[1],
                       'resistance': row[2],
		       'repetition': row[3],
		       'date': row[4],
	               'uuid': row[5]
		       }
	records_list.append(record_dict)
    result_dict = { 'records': records_list}	 
    return jsonify(result_dict)

