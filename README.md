#### LogSystem  
The design procedure should be database --> api --> program
####API Index
    post /body/train/
    Add records to database
    get /body/train/<date>
    Fetch records from database
    delete /body/train/<uuid>
    delete record from database
    get /body/calender
    Fetch training calender
    get /body/catalog
    Fetch catalog information
####Database scheme
Table main:  

id | record\_id | exercise\_id | catalog\_id | resistance | repetition | group | date | created\_at 
----- | ----- | ------------ | ----------- | ---------- | ---------- | ----- | -----| -----------
int | uuid | uuid | uuid | int | int | group | date | datetime
Examples:  
The unit of resistance is gram  
The format of date is : 2015-12-03  
The format of created\_at is not decided  

Table exercise:

id | exercise\_id | name | catalog_id
---- | ---- | ---- | ----
int | uuid | string | uuid

Table catalog:

id | catalog\_id | name
---- | ---- | ----
int | uuid | string

Table user:  

id | user\_id | name | password
---- | ---- | ---- | ----
int | uuid | string | string
