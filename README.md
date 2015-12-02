#### LogSystem
~~test~~ 
Add 组数，年月日，但是分条记录  
返回值add 动作名+部位名+时间
####Database scheme

Table main:  

id | record\_id | exercise\_id | catalog\_id | resistance | repetition | group | date | created\_at 
----- | ----- | ------------ | ----------- | ---------- | ---------- | ----- | -----| -----------
int | uuid | uuid | uuid | int | int | group | date | datetime
Examples:  
The unit of resistance is gram  
The format of date is : 2015-12-03  
The format of created\at is not decided  

Table exercise:

id | exercise\_id | name | catalog_id
---- | ---- | ---- | ----
int | uuid | string | uuid

Table catalog:

id | catalog\_id | name
---- | ---- | ----
int | uuid | string

####API

Get training record(s) 

**GET**`/body/train`

Request:  
Header:`date : 2015-12-03`
Response:  
Body:  
```
{
	"catalog": [
		"{
			“name": "胸部",
			"uuid": "de305d54-75b4-431b-adb2-eb6b9e546014",
			[
				{
					"name": "卧推",
					"uuid": "de305d54-75b4-431b-adb2-eb6b9e546014"
				}，
				{
					"name": "哑铃飞鸟",
					"uuid": "de305d54-75b4-431b-adb2-eb6b9e546014"
				}
			]
		},
		{
			“name": "背部",
			"uuid": "de305d54-75b4-431b-adb2-eb6b9e546014",
			[
				{
					"name": "哑铃俯身划船",
					"uuid": "de305d54-75b4-431b-adb2-eb6b9e546014"
				}，
				{
					"name": "史密斯机俯身划船",
					"uuid": "de305d54-75b4-431b-adb2-eb6b9e546014"
				}
			]
		},
	],
	"records"：[
		{
				"exercise": "卧推",
				"catalog": "胸部",
				"resistance": 140000,
				"repetition": 8,
				"date": "2015-11-29",
				"uuid": "0dca7d12-96b1-11e5-99ca-024d03c2f759"
		},
		{
				"exercise": "背部",
				"catalog": "哑铃俯身划船",
				"resistance": 140000,
				"repetition": 8,
				"date": "2015-11-29",
				"uuid": "0dca7d12-96b1-11e5-99ca-024d03c2f759"
		}
	]
}
```
**POST**`/body/train`  
Add a training record
Request:  
Header:`?`  
Body:  
```
{
	"name": "Dead lift",
	"part": "back",
	"weight": 30,
	"times": 8
}
```
Parameter | Type
------------ | -------------
name | xsd:string
part | xsd:string
weight | xsd:int
times | xsd:int
Response:  
Header:`?`  
Body:  
```
{
	"name": "Dead lift",
	"part": "back",
	"weight": 30,
	"times": 8,
	"created_at": "2015-11-29 15:51:28.942323",
	"uuid": "0dca7d12-96b1-11e5-99ca-024d03c2f759"
}
```
Parameter | Type
------------ | -------------
name | xsd:string
part | xsd:string
weight | xsd:int
times | xsd:int
created_at | xsd:dataTime
uuid | xsd:string
