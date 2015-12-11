import json
import sqlite3
from datetime import datetime
from flask import request
from flask import jsonify
from flask import json
from translator import uid2exercise, uid2catalog

def getResponse(request):
   
    connection = sqlite3.connect('/home/linaro/LogSystem/test.db')
    cur = connection.cursor()
    result = cur.execute("SELECT catalog_id,name from catalog;")
    catalog_list = []
    for row in result:
        
	cur2 = connection.cursor()
        result2 = cur2.execute("SELECT exercise_id,name from exercise where catalog_id = '%s' ;" % row[0])
	exercise_list = []
	for row2 in result2:
	    
	    exercise_dict = {
			    'name': row2[1],
                            'uuid': row2[0]
                            }
            exercise_list.append(exercise_dict)
	catalog_dict = {
		       'name': row[1],
		       'uuid': row[0],
                       'exercise': exercise_list
		       }
	catalog_list.append(catalog_dict)

    result_dict = { 'catalog': catalog_list}	 
    return jsonify(result_dict)

