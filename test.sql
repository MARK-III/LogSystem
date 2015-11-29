DROP TABLE main;
CREATE TABLE main (
uuid varchar(36),
name varchar(30),
part varchar(30),
weight integer,
times integer,
created_at text
);
DROP TABLE action;
CREATE TABLE action (
uuid varchar(36),
name varchar(30),
part varchar(36)
);
DROP TABLE part;
CREATE TABLE part (
uuid varchar(36),
name varchar(30),
);

