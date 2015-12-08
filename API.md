####API

Get training record(s) 

**GET**`/body/records/2015-12-03`

Request:  
Header:`?`
Response:  
Body:  
```
{
	"catalog": [
		{
			“name": "胸部",
			"uuid": "de305d54-75b4-431b-adb2-eb6b9e546014",
			"excersice": [
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
			"excersice": [
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

Add a training record

**POST**`/body/train`  

Request:  
Header:`?`  
Body:  
```
{
	"date": "2015-12-03",
	"records": [
		{
			"exercise": "硬拉",
			"catalog": "背部",
			"resistance": 30,
			"repitation": 8,
			"groups": 4
		},
		{
			"exercise": "硬拉",
			"catalog": "背部",
			"resistance": 30,
			"repitation": 8,
			"groups": 4
		}
	]
}
```
Response:  
Header:`?`  
Body:  
```
{
	"records": [
		{
			"exercise": "硬拉",
			"catalog": "背部",
			"resistance": 30,
			"repitation": 8,
			"groups": 4,
			"date": "2015-12-03",
			"uuid": "0dca7d12-96b1-11e5-99ca-024d03c2f759"
		},
		{
			"exercise": "硬拉",
			"catalog": "背部",
			"resistance": 30,
			"repitation": 8,
			"groups": 4,
			"date": "2015-12-03",
			"uuid": "0dca7d12-96b1-11e5-99ca-024d03c2f759"
		}
	]
}
```
