from uuid import uuid1
import sqlite3 

def uid2catalog(uid):
    
    connection = sqlite3.connect('/home/linaro/LogSystem/test.db')
    cur = connection.cursor()
    cur.execute("SELECT name FROM catalog WHERE catalog_id = '%s'" % uid)
    result = cur.fetchone()
    if result is None:
	return 'Name not found'
    else:
	return str(result[0])  
   

def catalog2uid(name):
 
    connection = sqlite3.connect('/home/linaro/LogSystem/test.db')
    cur = connection.cursor()
    cur.execute("SELECT catalog_id FROM catalog WHERE name = '%s'" % name)
    result = cur.fetchone() 
    if result is None:
	uid = str(uuid1())
	cur.execute("INSERT INTO catalog VALUES ('%s', '%s')" % (uid, name))
        connection.commit()
	connection.close()
	return uid
    else:
	return str(result[0])

def uid2exercise(uid):
    
    connection = sqlite3.connect('/home/linaro/LogSystem/test.db')
    cur = connection.cursor()
    cur.execute("SELECT name FROM exercise WHERE exercise_id = '%s'" % uid)
    result = cur.fetchone()
    if result is None:
	return 'Name not found'
    else:
	return str(result[0])  

def exercise2uid(name,name2):
   
    connection = sqlite3.connect('/home/linaro/LogSystem/test.db')
    cur = connection.cursor()
    cur.execute("SELECT exercise_id FROM exercise WHERE name = '%s'" % name)
    result = cur.fetchone() 
    if result is None:
	catalog_uid = catalog2uid(name2)
	uid = str(uuid1())
	cur.execute("INSERT INTO exercise VALUES ('%s', '%s', '%s')" % (uid, name, catalog_uid))
        connection.commit()
	connection.close()
	return uid
    else:
	return str(result[0])


