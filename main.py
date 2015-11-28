import sqlite3
import uuid
import backend
from datetime import datetime

uid = str(uuid.uuid1())
name = 'Dead lift'
weight = 30
times = 8
datetime = str(datetime.now())
t = (uid,name,weight,times,datetime,)
print(t)
conn = sqlite3.connect('test.db')
c = conn.cursor()

c.execute('INSERT INTO main VALUES(?,?,?,?,?)',t)
conn.commit()
conn.close()

