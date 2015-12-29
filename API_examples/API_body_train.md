Add a training record

**POST**`/body/train`  

Request:  
Header:`?`  
Body:  
```
{
    "records": [
        {
            "exercise": "aaa",
            "catalog": "Leg",
            "resistance": 30,
            "repitation": 8,
            "date": "2015-12-30",
            "tagid": "123",
            "groups": "4"
        },
        {
            "exercise": "bb",
            "catalog": "Back",
            "resistance": 30,
            "repitation": 8,
            "date": "2015-12-30",
            "tagid": "456",
            "groups": "4"
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
            "catalog": "Leg",
            "date": "2015-12-30",
            "exercise": "aaa",
            "repetition": 8,
            "resistance": 30,
            "tagid": "123",
            "uuid": "0e2e2b1e-ae8a-11e5-a597-024d03c2f759"
        },
        {
            "catalog": "Leg",
            "date": "2015-12-30",
            "exercise": "aaa",
            "repetition": 8,
            "resistance": 30,
            "tagid": "123",
            "uuid": "0e30f95c-ae8a-11e5-a597-024d03c2f759"
        },
        {
            "catalog": "Leg",
            "date": "2015-12-30",
            "exercise": "aaa",
            "repetition": 8,
            "resistance": 30,
            "tagid": "123",
            "uuid": "0e32f00e-ae8a-11e5-a597-024d03c2f759"
        },
        {
            "catalog": "Leg",
            "date": "2015-12-30",
            "exercise": "aaa",
            "repetition": 8,
            "resistance": 30,
            "tagid": "123",
            "uuid": "0e35bc4e-ae8a-11e5-a597-024d03c2f759"
        },
        {
            "catalog": "Back",
            "date": "2015-12-30",
            "exercise": "bb",
            "repetition": 8,
            "resistance": 30,
            "tagid": "456",
            "uuid": "0e3dc9fc-ae8a-11e5-a597-024d03c2f759"
        },
        {
            "catalog": "Back",
            "date": "2015-12-30",
            "exercise": "bb",
            "repetition": 8,
            "resistance": 30,
            "tagid": "456",
            "uuid": "0e40cc56-ae8a-11e5-a597-024d03c2f759"
        },
        {
            "catalog": "Back",
            "date": "2015-12-30",
            "exercise": "bb",
            "repetition": 8,
            "resistance": 30,
            "tagid": "456",
            "uuid": "0e43adea-ae8a-11e5-a597-024d03c2f759"
        },
        {
            "catalog": "Back",
            "date": "2015-12-30",
            "exercise": "bb",
            "repetition": 8,
            "resistance": 30,
            "tagid": "456",
            "uuid": "0e4734ec-ae8a-11e5-a597-024d03c2f759"
        }
    ]
}
```
