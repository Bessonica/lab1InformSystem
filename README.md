# lab 1 project 
information system for library

we have books and magazines table
## Books:
 - name, genre, year

## Magazines:
 - title, issue, issueTitle

We have to export 3 rows from sqlite into mySQL database and export 2 rows into postgSQL (17 вариант)

package used, used virtual env:
- mysql-connector==2.2.9
- mysql-connector-python==8.0.29
- peewee==3.15.0
- protobuf==4.21.2
- psycopg2==2.9.3
- pymongo==4.1.1
- PyMySQL==1.0.2

start program from start.py( python start.py)

## SQLight
We have two sqLight databases (dataBaseBooks_Sqlite, dataBaseMagazines_Sqlite).They are created in **setupDB.py file**
- names of db:  magazines.db, books.db
Each one of them have 1 table.(books, magazines)

## mySQL
mySQL database (dataBaseBooks_mySQL) from **setupMysql.py**
- name: test
- tables: (books1, magazines1)

constructor has method to create table and to drop all rows(it is made
so rows would not duplicate, when launch again):
- createTableBooks, createDataBase
- dropTableMagazines1, dropTableBooks1

## postgreSQL
in postgreSQL we have database test. **setupPostgSQL.py**
- name: test
- tables: (books1, magazines1)

## functions in start.py
1. function, responsible for SQLight -> mySQL:  **insertSQLightIntoMysql** 
2. function, responsible for mySQL -> postgreSQL: **insertMysqlToPostgreSQL**
3. you can find them in file (exportDB.py)


functions, responsible for tree management 
- treebook_***  (add, update, delete)
- treemagaz_*** (add, update, delete))

# Screenshots