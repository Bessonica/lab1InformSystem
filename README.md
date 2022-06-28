# lab 1 project 
information system for library

we have books and magazines table
## Books:
 - name, genre, year

## Magazines:
 - title, issue, issueTitle

We have to export 3 rows from sqlite into mySQL database and export 2 rows into postgSQL (17 вариант)

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
