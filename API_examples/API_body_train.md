Add a training record

**POST**`/body/train`  

Request:  
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
			"groups": 1，
			"date": "2015-12-03"
		},
		{
			"exercise": "硬拉",
			"catalog": "背部",
			"resistance": 30,
			"repitation": 8,
			"groups": 1，
			"date": "2015-12-03"
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
			"date": "2015-12-03",
			"uuid": "0dca7d12-96b1-11e5-99ca-024d03c2f759"
		},
		{
			"exercise": "硬拉",
			"catalog": "背部",
			"resistance": 30,
			"repitation": 8,
			"date": "2015-12-03",
			"uuid": "0dca7d12-96b1-11e5-99ca-024d03c2f759"
		}
	]
}
```
