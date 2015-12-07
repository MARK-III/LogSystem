import json
import uuid
import sqlite3
from datetime import datetime
from flask import request
from flask import jsonify

def getResponse(request):
    
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
    return jsonify(json_dict)
