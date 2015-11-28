import json
import uuid
import sqlite3
from datetime import datetime

def post_train(content):
    uid = str(uuid.uuid1())
    name = 'Dead lift'
    weight = 30
    times = 8
    date_time = str(datetime.now())
    data = (uid,name,weight,times,date_time)
    connection = sqlite3.connect('test.db')
    cur = connection.cursor()
    cur.execute('INSERT INTO main VALUES(?,?,?,?,?)',data)
    connection.commit()
    connection.close()

    return content
