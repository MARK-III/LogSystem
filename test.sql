DROP TABLE main;

CREATE TABLE main (
record_id varchar(36),
exercise_id varchar(30),
catalog_id varchar(30),
resistance integer,
repetition integer,
date varchar(10),
created_at varchar(50)
);

DROP TABLE exercise;

CREATE TABLE exercise (
exercise_id varchar(36),
name varchar(50),
catalog_id varchar(36)
);

DROP TABLE catalog;

CREATE TABLE catalog (
catalog_id varchar(36),
name varchar(50)
);

DROP TABLE user;

CREATE TABLE user (
user_id varchar(36),
name varchar(50),
password string
);

