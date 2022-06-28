import mysql.connector
import sqlite3

from setupDB import dataBaseBooks_Sqlite
from setupDB import dataBaseMagazines_Sqlite

from setupMysql import dataBaseBooks_mySQL
from setupPostgSQL import dataBasePostg

dbSQLightBooks = dataBaseBooks_Sqlite()
dbSQLightMagazines = dataBaseMagazines_Sqlite()
#!!!!
#dont forget change db(right now is test)
# clear table, so there would be no duplicate
#!!!!

# db1  sqlite
# db2  mysql

#   INSERT INTO books (name, genre, year) VALUES (%s, %s, %s)

#   this is how we insert data
# mySQLcursor.execute(  "INSERT INTO books (name, genre, year) VALUES ('yo', 'yo', 40)" )
# mySQLdb.commit()

def insertSQLightIntoMysql(table1, table2, mySQlCur, mySQLdb):
    mySQlCur.execute("DELETE FROM books1")
    mySQlCur.execute("DELETE FROM magazines1")

    rowBooks = table1.show()
    rowMagazines = table2.show()

    print("rows in books")
    for rows in rowBooks:
        print(rows)
        
    print("rows in magazines")
    for rows in rowMagazines:
        print(rows)

    #insert into mysql books
    print("insert data into mysql books")
    for rows in rowBooks:
        arg1 = "INSERT INTO books1 (name, genre, year) VALUES (%s, %s, %s)"
        arg2 = (rows[1], rows[2], rows[3])
        mySQlCur.execute(arg1, arg2)
        mySQLdb.commit()

    #insert into my sql magazines
    print("insert data into mysql magazines")
    for rows in rowMagazines:
        arg1 = "INSERT INTO magazines1 (title, issue, issueTitle) VALUES (%s, %s, %s)"
        arg2 = (rows[1], rows[2], rows[3])
        mySQlCur.execute(arg1, arg2)
        mySQLdb.commit()

#  def insertMysqlToPostgreSQL(mySQLDB, postSQLDB, mySQlCur, mySQLdb, postSQLcur, postSQLcon):

def insertMysqlToPostgreSQL(mySQLDB, postSQLcur, postSQLcon):
    # !!!! clean postgreSQL
    # postSQLcur.execute("TRUNCATE TABLE books1, magazines1;")
    # postSQLcon.commit()
    # postSQLcur.close()
    # postSQLcur.execute("TRUNCATE TABLE magazines1;")
    # postSQLcon.commit()

    postSQLcur.execute("DELETE FROM books1")
    postSQLcon.commit()
    postSQLcur.execute("DELETE FROM magazines1")
    postSQLcon.commit()
    print("mySQL")
    print(mySqlDB)


    rowBooks = mySQLDB.showBooks()
    rowMagazines = mySQLDB.showMagazines()
    
    print("rowBooks myssql - postSQL")
    for rows in rowBooks:
        print(rows)

    print("rowMagazines myssql - postSQL")
    for rows in rowMagazines:
        print(rows)


    for rows in rowBooks:
        arg1 = "INSERT INTO books1 (name, year) VALUES(%s, %s)"
        arg2 = (rows[0], rows[2])
        postSQLcur.execute(arg1, arg2)
        postSQLcon.commit()


    for rows in rowMagazines:
        arg1 = "INSERT INTO magazines1 (title, issue) VALUES(%s, %s)"
        arg2 = (rows[0], rows[1])
        postSQLcur.execute(arg1, arg2)
        postSQLcon.commit()


    postSQLcur.close()
    postSQLcon.close()




    
    
# print("sqLight")
# print(dbSQLightBooks.show())

# rowBooks = dbSQLightBooks.show()

# for rows in rowBooks:
#     print(rows)
#     for el in rows:
#         print(el)
   

# mySQLdb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='agoptq',
#     auth_plugin='mysql_native_password',
#     database = 'test'
# )

# print("databases")
# mySQLcursor = mySQLdb.cursor()


mySqlDB = dataBaseBooks_mySQL()

mySQLcur = mySqlDB.mySQLcursor
mySQLcon = mySqlDB.mySQLdb
# print("my SQL magazines")
# print(mySqlDB.showMagazines())


postSQLDB = dataBasePostg()
postSQLcur = postSQLDB.cur
postSQLcon = postSQLDB.pSQLconn
# print(postSQLDB.show())

#mySQLdb

#     create tables
#mySQLcursor.execute("CREATE TABLE books1 (name VARCHAR(255), genre VARCHAR(255), year VARCHAR(255), book_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
# mySQLcursor.execute("CREATE TABLE magazines1 (title VARCHAR(255), issue VARCHAR(255), issueTitle VARCHAR(255), book_id INTEGER AUTO_INCREMENT PRIMARY KEY)")


# insertSQLightIntoMysql(dbSQLightBooks, dbSQLightMagazines, mySQLcur, mySQLcon)


# insertMysqlToPostgreSQL(mySqlDB,  postSQLcur, postSQLcon)


# mySQLcursor.execute("SHOW DATABASES")
# for db in mySQLcursor:
#     print(db)




# print("tables")
# mySQLcursor.execute("SHOW TABLES")
# for table in mySQLcursor:
#     print(table)

