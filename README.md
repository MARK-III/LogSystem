#### LogSystem
####Database structure
table main  

id | name | wight | times | created_at 
-------- | ---------- | -------- | -------- | ----------
int | string | int | int | dataTime
####API
**POST**`/body/train`  
Add a training record  
```
{
	"name": "Dead lift",
	"weight": 30,
	"times": 8
}
```
Parameter | Type
------------ | -------------
name | xsd:string
weight | xsd:int
times | xsd:int
created_at | xsd:dataTime
id | xsd:int
```
{
	"status": "recorded",
	"name": "Dead lift",
	"weight": 30,
	"created_at": "2015-11-27T00:12:55Z",
	"id": 1
}
```
Parameter | Type
------------ | -------------
status | xsd:string
name | xsd:string
weight | xsd:int
times | xsd:int
created_at | xsd:dataTime
id | xsd:int
