import sqlite3
import uuid
import backend
from datetime import datetime
import json
from flask import jsonify

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

response = json.JSONEncoder().encode(json_dict)
print(response)

