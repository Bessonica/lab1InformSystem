import sqlite3


class dataBaseBooks_Sqlite:
    def __init__(self):
        self.db = sqlite3.connect("books.db")
        self.cursor = self.db.cursor()
        self.createTable()


    def createTable(self):
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS books (id integer PRIMARY KEY AUTOINCREMENT, name text NOT NULL, genre text NOT NULL, year int); """)

    def dropTable(self):
        self.cursor.execute(""" DELETE FROM books; """)

        


    def show(self):
        self.cursor.execute("""SELECT * FROM books """)
        self.rows = self.cursor.fetchall()
        return self.rows

        



    






class dataBaseMagazines_Sqlite:
    def __init__(self):
        self.dbM = sqlite3.connect("magazines.db")
        self.cursorM = self.dbM.cursor()
        self.createTable()


    def createTable(self):
        self.cursorM.execute(""" CREATE TABLE IF NOT EXISTS magazines (id integer PRIMARY KEY AUTOINCREMENT, title text NOT NULL, issue text NOT NULL, issueTitle text NOT NULL); """)

    def show(self):
        self.cursorM.execute("""SELECT * FROM magazines """)
        self.rows = self.cursorM.fetchall()
        return self.rows

    def dropTable(self):
        self.cursorM.execute(""" DELETE FROM magazines; """)





##unfinished method for sqLight management

    # def sqlData_add(self, dataBaseName, arg1, arg2, arg3):
    #     print("deez nuts")
    #     self.database1 = "books"
    #     self.database2 = "magazines"


    #     print("book add args")
    #     print(arg1, arg2, arg3)

    # # зачем этот каунт тут ????
    #     self.cursor.execute("SELECT COUNT(*) from books WHERE name = '" +
    #     arg1 +"' ")
    #     self.result = self.cursor.fetchone()

    # # if dataBaseName == "books":
    # #     pass

    #     if int(self.result[0]) > 0:
    #         print("error")
    #         print(result[0])
    #     elif self.dataBaseName == "books":
    #         self.cursor.execute("INSERT INTO '" + str(database1) +"'(name, genre, year) VALUES(?, ?, ?)", (arg1, arg2, arg3))
    #         self.db.commit()
    #         print("added to books")
    #     elif self.dataBaseName == "magazines":
    #         self.cursorM.execute("INSERT INTO '" + str(database2) +"'(title, issue, issueTitle) VALUES(?, ?, ?)", (arg1, arg2, arg3))
    #         self.dbM.commit()