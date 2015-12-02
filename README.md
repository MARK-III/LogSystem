#### LogSystem
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
