import json
import uuid
import sqlite3
from datetime import datetime

def post_body_train(body):

    uid = str(uuid.uuid1())
    exercise = 'dd'
    part = 'back'
    weight = 30
    times = 8
    date_time = str(datetime.now())
    data = (uid,name,part,weight,times,date_time)
    
    connection = sqlite3.connect('test.db')
    cur = connection.cursor()
    cur.execute('INSERT INTO main VALUES(?,?,?,?,?,?)',data)
    connection.commit()
    connection.close()

    json_dict = {'name': name,
		 'part': part,
		 'weight': weight,
		 'times': times,
		 'created_at': date_time,
		 'uuid': uid}
    return json_dict

def get_body_train():
    
    dict1 = {
                "excercise": "Dead Lift",
		"catalog": "Back",
		"resistance": 30,
		"repitation": 8,
		"group": 4,
		"date": "2015-12-03",
		"uuid": "0dca7d12-96b1-11e5-99ca-024d03c2f759"
	    }
    dict2 = {
                "excercise": "Dead Lift",
                "catalog": "Back",
                "resistance": 30,
                "repitation": 8,
                "group": 4,
                "date": "2015-12-03",
                "uuid": "0dca7d12-96b2-11e5-99ca-024d03c2f759"
            }
    array1 = [dict1,dict2]
    json_dict = {'records': array1}
    return json_dict
