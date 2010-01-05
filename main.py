import sqlite3
import uuid
from datetime import datetime
import json
from flask import jsonify
import os

path = '/home/linaro/LogSystem/test.db'
exist = os.path.isfile(path)
if exist:
    print('exist')
else:
    print('not')
