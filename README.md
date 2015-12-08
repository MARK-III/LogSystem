#### LogSystem  
The design procedure should be database --> api --> program
####API Index
    post /body/train/........implemented
    Add records to database
    
    get /body/records/<date>.......implemented
    Fetch records from database
    
    delete /body/record/<uuid>.......not yet
    delete record from database
    
    get /body/calender........not yet
    Fetch training calender
    
    get /body/catalog.......not yet
    Fetch catalog information
    
####Database scheme
Table main:  

id | record\_id | exercise\_id | catalog\_id | resistance | repetition | date | created\_at 
----- | ----- | ------------ | ----------- | ---------- | ---------- | -----| -----------
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
