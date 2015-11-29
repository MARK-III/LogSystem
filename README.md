#### LogSystem
####Database structure
table main  

id | name | wight | times | created_at 
-------- | ---------- | -------- | -------- | ----------
int | string | int | int | dateTime
####API
**POST**`/body/train`  
Add a training record  
```
{
	"name": "Dead lift",
	"type": "back",
	"weight": 30,
	"times": 8
}
```
Parameter | Type
------------ | -------------
name | xsd:string
type | xsd:string
weight | xsd:int
times | xsd:int
```
{
	"status": "recorded",
	"name": "Dead lift",
	"type": "back",
	"weight": 30,
	"times": 8,
	"created_at": "2015-11-27T00:12:55Z",
	"uuid": xxxx
}
```
Parameter | Type
------------ | -------------
status | xsd:string
name | xsd:string
type | xsd:string
weight | xsd:int
times | xsd:int
created_at | xsd:dataTime
uuid | xsd:string
