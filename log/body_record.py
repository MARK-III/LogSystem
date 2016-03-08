import json
import sqlite3
from datetime import datetime
from flask import request
from flask import jsonify
from flask import json
from translator import uid2exercise, uid2catalog

def getResponse(request,uuid):
   
    connection = sqlite3.connect('/home/linaro/LogSystem/test.db')
    cur = connection.cursor()
    cur.execute("DELETE from main where record_id = '%s'" % uuid)
    connection.commit()
    connection.close()
    result_dict = { 'uuid': uuid}	 
    return jsonify(result_dict)

