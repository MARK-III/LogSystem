from flask import request
from flask import jsonify
from flask import json
from datetime import datetime
from uuid import uuid1
import sqlite3

def getResponse(request):

    body = request.get_json(force = True, silent = True)
    date = body['date']
    time = datetime.now()
    records_list = []
    for record in body['records']:
	
	for i in range(0, record['groups']):

            exercise = record['exercise']
	    catalog = record['catalog']
	    resistance = record['resistance']
	    repitation = record['repitation']
	    uid = str(uuid1())
	
	    data = (uid,exercise,catalog,resistance,repitation,date,time)
	    connection = sqlite3.connect('test.db')
	    cur = connection.cursor()
	    cur.execute('INSERT INTO main VALUES(?,?,?,?,?,?,?)',data)
    	    connection.commit()
    	    connection.close()
            record_dict = {
                           'exercise': exercise,
                           'catalog': catalog,
                           'resistance': resistance,
                           'repetition': repitation,
                           'date': date,
                           'uuid': uid
                           }
            records_list.append(record_dict)
    result_dict = { 'records': records_list}
    return jsonify(result_dict)
