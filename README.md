# LogSystem
Database structure



API

POST	/body/train	Record training

{
	"name": "Dead lift",
	"weight": 30,
	"times": 8
}

Request parameters

name	xsd:string
weight	xsd:int
times	xsd:int

{
	"status": "recorded",
	"name": "Dead lift",
	"weight": 30,
	"created_at": "2015-11-27T00:12:55Z",
	"id": 1
}

Response parameters

status	xsd:string
weight	xsd:int
times	xsd:int
created_at	xsd:dataTime
id	xsd:int	
