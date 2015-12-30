#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import request
from flask import jsonify
from flask import json
from datetime import datetime
from uuid import uuid1
import sqlite3
from translator import catalog2uid, exercise2uid

def getResponse(request):

    body = request.get_json(force = True, silent = True)
    #date = body['date']
    time = datetime.now()
    records_list = []
    for record in body['records']:
	
	for i in range(0, int(record['groups'])):

	    catalog = record['catalog']
	    catalog_id = catalog2uid(catalog)
            exercise = record['exercise']
	    exercise_id = exercise2uid(exercise, catalog)
	    resistance = record['resistance']
	    repetition = record['repetition']
	    date = record['date']
            tagid = record['tagid']
	    uid = str(uuid1())
	
	    data = (uid,exercise_id,catalog_id,resistance,repetition,date,time)
	    connection = sqlite3.connect('test.db')
	    cur = connection.cursor()
	    cur.execute('INSERT INTO main VALUES(?,?,?,?,?,?,?)',data)
    	    connection.commit()
    	    connection.close()
            record_dict = {
                           'exercise': exercise,
                           'catalog': catalog,
                           'resistance': resistance,
                           'repetition': repetition,
                           'date': date,
                           'uuid': uid,
			   'tagid': tagid
                           }
            records_list.append(record_dict)
    result_dict = { 'records': records_list}
    return jsonify(result_dict)
