import json
import sqlite3
from flask import request
from flask import jsonify
from flask import json

def getResponse(request,date):
   
    connection = sqlite3.connect('/home/linaro/LogSystem/test.db')
    cur = connection.cursor()
    result = cur.execute("SELECT date from main where date like '%s___'" % date)

    day_set = set()
    for row in result:

        day = row[0][9:10]
	day_set.add(day)
    day_list = list(day_set)
    result_dict = { 'days': day_list}	 
    return jsonify(result_dict)

