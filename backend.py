import json
import uuid
import sqlite3
from datetime import datetime

def post_train(content):
    
    uid = str(uuid.uuid1())
    name = 'Dead lift'
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

def get_train():
    
    name = 'Dear lift'
    part = 'back'
    weight = 30
    times = 8
    date_time = '2015-11-27T00:12:55Z'
    uuid = 'xxxx'
    json_dict = {'name': name,
		 'part': part,
		 'weight': weight,
		 'times': times,
		 'date_time': date_time,
		 'uuid': uuid}
    
    return json_dict
