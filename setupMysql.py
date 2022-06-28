import mysql.connector


#  this db has both tables 

class dataBaseBooks_mySQL:
    def __init__(self):
        self.mySQLdb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='agoptq',
            auth_plugin='mysql_native_password',
            database = 'test'
        )
        self.mySQLcursor = self.mySQLdb.cursor()
        #   dont forget about create table !!!!


    def createDataBase(self):
        self.mySQLcursor.execute("CREATE DATABASE test")

    def createTableBooks(self):
        self.mySQLcursor.execute("CREATE TABLE books1 (name VARCHAR(255), genre VARCHAR(255), year VARCHAR(255), book_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
        

    def createTableMagazines(self):
        self.mySQLcursor.execute("CREATE TABLE magazines1 (name VARCHAR(255), genre VARCHAR(255), year VARCHAR(255), book_id INTEGER AUTO_INCREMENT PRIMARY KEY)")

    def showBooks(self):
        self.mySQLcursor.execute("SELECT * FROM books1")
        self.rows = self.mySQLcursor.fetchall()
        return self.rows
        

    def showMagazines(self):
        self.mySQLcursor.execute("SELECT * FROM magazines1")
        self.rows = self.mySQLcursor.fetchall()
        return self.rows

    
    def dropTableMagazines1(self):
        self.mySQLcursor.execute(""" DELETE FROM magazines1; """)
        self.mySQLdb.commit()

    def dropTableBooks1(self):
        self.mySQLcursor.execute(""" DELETE FROM books1; """)
        self.mySQLdb.commit()








# create DB
# mySQLcursor.execute("CREATE DATABASE test")

#name, genre, year
# create table
#mySQLcursor.execute("CREATE TABLE books (name VARCHAR(255), genre VARCHAR(255), year INTEGER(10), book_id INTEGER AUTO_INCREMENT PRIMARY KEY)")