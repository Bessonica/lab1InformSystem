from select import select
from tkinter import *
from tkinter import ttk

import mysql.connector
# from gui.py import 

import sqlite3

from setupDB import dataBaseBooks_Sqlite
from setupDB import dataBaseMagazines_Sqlite

from gui import windowTK

from exportDB import insertSQLightIntoMysql
from exportDB import insertMysqlToPostgreSQL

from setupPostgSQL import dataBasePostg
postSQLDB = dataBasePostg()
postSQLcur = postSQLDB.cur
postSQLcon = postSQLDB.pSQLconn



dbBooks = dataBaseBooks_Sqlite()
dbMagazines = dataBaseMagazines_Sqlite()

#  delete all rows to avoid duplication
dbBooks.dropTable()
dbMagazines.dropTable()

from setupMysql import dataBaseBooks_mySQL
mySqlDB = dataBaseBooks_mySQL()


#  delete all rows to avoid duplication
mySqlDB.dropTableBooks1()
mySqlDB.dropTableMagazines1()


mySQLcur = mySqlDB.mySQLcursor
mySQLcon = mySqlDB.mySQLdb

# mySQLdb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='agoptq',
#     auth_plugin='mysql_native_password',
#     database = 'test'
# )
# mySQLcursor = mySQLdb.cursor()

# with sqlite3.connect("books.db") as db:
#     cursor = db.cursor()

# cursor.execute(""" CREATE TABLE IF NOT EXISTS books (id integer PRIMARY KEY AUTOINCREMENT, name text NOT NULL, genre text NOT NULL, year int); """)

# # cursor.execute(""" CREATE TABLE IF NOT EXISTS books (id integer PRIMARY KEY AUTOINCREMENT, name text NOT NULL, genre text NOT NULL); """)


# with sqlite3.connect("magazines.db") as dbM:
#     cursorM = dbM.cursor()

# cursorM.execute(""" CREATE TABLE IF NOT EXISTS magazines (id integer PRIMARY KEY AUTOINCREMENT, title text NOT NULL, issue text NOT NULL, issueTitle text NOT NULL); """)


db = dbBooks.db
cursor = dbBooks.cursor

dbM = dbMagazines.dbM
cursorM = dbMagazines.cursorM

def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

def read(databaseName):
    # conn = sqlite3.connect("data.db")
    # cursor = conn.cursor()

    # cursor.execute("""CREATE TABLE IF NOT EXISTS books (id integer PRIMARY KEY AUTOINCREMENT, name text NOT NULL, genre text NOT NULL); """)
    if databaseName == "books":
        cursor.execute("SELECT * FROM books")
        results = cursor.fetchall()
        db.commit()
    elif databaseName == "magazines":
        cursorM.execute("SELECT * FROM magazines")
        results = cursorM.fetchall()
        dbM.commit()


    
    
    # conn.commit()
   
    return results


def readM():
    cursorM.execute("SELECT * FROM magazines")
    results = cursorM.fetchall()
    # conn.commit()
    dbM.commit()
    return results


#----start   sqlite related   start

def sqlData_add(dataBaseName, arg1, arg2, arg3):
    print("deez nuts")
    database1 = "books"
    database2 = "magazines"


    print("book add args")
    print(arg1, arg2, arg3)

    # зачем этот каунт тут ????
    cursor.execute("SELECT COUNT(*) from books WHERE name = '" +
    arg1 +"' ")
    result = cursor.fetchone()

    # if dataBaseName == "books":
    #     pass

    if int(result[0]) > 0:
        print("error")
        print(result[0])
    elif dataBaseName == "books":
        cursor.execute("INSERT INTO '" + str(database1) +"'(name, genre, year) VALUES(?, ?, ?)", (arg1, arg2, arg3))
        db.commit()
        print("added to books")
    elif dataBaseName == "magazines":
        cursorM.execute("INSERT INTO '" + str(database2) +"'(title, issue, issueTitle) VALUES(?, ?, ?)", (arg1, arg2, arg3))
        dbM.commit()


def sqlData_delete(deleteID, databaseName):
    #find book in db by id
    if databaseName == "books":
        cursor.execute("DELETE FROM books WHERE id = '" + str(deleteID) + "'")
        db.commit()
    elif databaseName == "magazines":
        cursorM.execute("DELETE FROM magazines WHERE id = '" + str(deleteID) + "'")
        dbM.commit()
  

    
def sqlData_edit(updateID, databaseName, arg1, arg2, arg3):
    print("updated ID")
    print(updateID)

    # editBookID = bookID.get()

    # conn = sqlite3.connect("books.db")
    # cursor = conn.cursor()

    if databaseName == "books":
        cursor.execute("UPDATE books SET name = '" + str(arg1) + "', genre = '" + str(arg2) + "', year = '" + str(arg3) + "' WHERE id ='" + str(updateID) + "'")
        db.commit()
    elif databaseName == "magazines":
        cursorM.execute("UPDATE magazines SET title = '" + str(arg1) + "', issue = '" + str(arg2) + "', issueTitle = '" + str(arg3) + "' WHERE id ='" + str(updateID) + "'")
        dbM.commit()

    # cursor.execute("UPDATE books SET name = '" + str(editBookName) + "', genre = '" + str(editBookGenre) + "', year = '" + str(editBookYear) + "' WHERE id ='" + str(updateID) + "'")
    # db.commit()


# cursor.execute("UPDATE inventory SET itemId = '" "', itemName = '" + str(name) + "', itemPrice = '" + str(price) + "', itemQuantity = '" + str(quantity) + "' WHERE itemId='"+str(idName)+"'")

# ----end   sqlite related   


#----start   tree related
def treebook_add():

    newBookName = bookName.get()
    newBookGenre = bookGenre.get()
    newBookYear = bookYear.get()

    # here we give database name
    sqlData_add("books", newBookName, newBookGenre, newBookYear)


    #  why this part here????
    for data in tree.get_children():
        tree.delete(data)


    for result in reverse(read("books")):
        tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")


def treebook_update():
    selected_item = tree.selection()[0]
    updateID = tree.item(selected_item)['values'][0]
    
    editBookName = bookName.get()
    editBookGenre = bookGenre.get()
    editBookYear = bookYear.get()
    sqlData_edit(updateID, "books", editBookName, editBookGenre, editBookYear)

      # update tree
    for data in tree.get_children():
        tree.delete(data)


    for result in reverse(read("books")):
        tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    
    


def treebook_delete():
    selected_item = tree.selection()[0]
    deleteID = tree.item(selected_item)['values'][0]
    sqlData_delete(deleteID, "books")

          # update tree
    for data in tree.get_children():
        tree.delete(data)


    for result in reverse(read("books")):
        tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    
#     MAGAZINE PART
def treemagaz_add():
    newMagazTitle = magazineName.get()
    newMagazIssue = magazineIssue.get()
    newMagazIssueTitle = magazineIssueTitle.get()
    dataBaseName = "magazines"

    print("magaz data")
    print(newMagazTitle, newMagazIssue, newMagazIssueTitle)
    sqlData_add(dataBaseName, newMagazTitle, newMagazIssue, newMagazIssueTitle)

    for data in treeMagaz.get_children():
        treeMagaz.delete(data)


    for result in reverse(read("magazines")):
        treeMagaz.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")



def treemagaz_update():
    selected_item = treeMagaz.selection()[0]
    updateID = treeMagaz.item(selected_item)['values'][0]
    print(updateID)

    newMagazTitle = magazineName.get()
    newMagazIssue = magazineIssue.get()
    newMagazIssueTitle = magazineIssueTitle.get()
    dataBaseName = "magazines"
    sqlData_edit(updateID, "magazines", newMagazTitle, newMagazIssue, newMagazIssueTitle)


    for data in treeMagaz.get_children():
        treeMagaz.delete(data)


    for result in reverse(read("magazines")):
        treeMagaz.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")


    

def treemagaz_delete():
    selected_item = treeMagaz.selection()[0]
    deleteID = treeMagaz.item(selected_item)['values'][0]
    sqlData_delete(deleteID, "magazines")

          # update tree
    for data in treeMagaz.get_children():
        treeMagaz.delete(data)


    for result in reverse(read("magazines")):
        treeMagaz.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    


#----end   tree related




#  create window
window = Tk()
window.geometry("1200x720")


#new
# window = windowTK().window
# window = windowTK().window


# old
# book tree
tree = ttk.Treeview(window)

tree['columns'] = ("ID", "Title", "Genre", "Year")

tree.column("#0", width=0, stretch=NO)
tree.column("ID", anchor=W, width=100)
tree.column("Title", anchor=W, width=200)
tree.column("Genre", anchor=W, width=150)
tree.column("Year", anchor=W, width=150)

tree.heading("ID", text="ID", anchor=W)
tree.heading("Title", text="Title", anchor=W)
tree.heading("Genre", text="Genre", anchor=W)
tree.heading("Year", text="Year", anchor=W)


tree.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 15))
tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)


# magazine tree
treeMagaz = ttk.Treeview(window)

treeMagaz['columns'] = ("ID", "Title", "Issue", "Issue title")

treeMagaz.column("#0", width=0, stretch=NO)
treeMagaz.column("ID", anchor=W, width=100)
treeMagaz.column("Title", anchor=W, width=200)
treeMagaz.column("Issue", anchor=W, width=150)
treeMagaz.column("Issue title", anchor=W, width=150)

treeMagaz.heading("ID", text="ID", anchor=W)
treeMagaz.heading("Title", text="Title", anchor=W)
treeMagaz.heading("Issue", text="Issue", anchor=W)
treeMagaz.heading("Issue title", text="Issue title", anchor=W)

treeMagaz.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 15))
treeMagaz.grid(row=10, column=5, columnspan=4, rowspan=5, padx=10, pady=10)



        #upddate magazine tree
for data in treeMagaz.get_children():
    treeMagaz.delete(data)

for result in reverse(readM()):
    treeMagaz.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")



    
        #upddate book tree
for data in tree.get_children():
    tree.delete(data)

for result in reverse(read("books")):
    tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

        


#    export data to another   DB
def exportSQLight():
    insertSQLightIntoMysql(dbBooks, dbMagazines,mySQLcur, mySQLcon)
    

def exportMySQL():
    insertMysqlToPostgreSQL(mySqlDB, postSQLcur, postSQLcon)


#-----START    GUI
#enter magazine title
labelBookM1 = Label(text="Enter magazine title")
labelBookM1.place(x = 30, y = 40)
labelBookM1.config(bg='lightgreen', padx = 0)
labelBookM1.grid(row=10, column=0, padx=10, pady=10)

magazineName = Entry(text = "")
magazineName.place(x = 150, y =40, width = 200, height = 25)
magazineName.grid(row= 10, column=1, columnspan=3, padx=2, pady=2)


labelBookM2 = Label(text="Enter magazine issue")
labelBookM2.place(x = 30, y = 70)
labelBookM2.config(bg='lightgreen', padx = 0)
labelBookM2.grid(row=11, column=0, padx=10, pady=10)

magazineIssue = Entry(text = "")
magazineIssue.place(x = 150, y =70, width = 200, height = 25)
magazineIssue.grid(row=11, column=1, columnspan=3, padx=2, pady=2)

labelBookM3 = Label(text="Enter issue title")
labelBookM3.place(x = 30, y = 100)
labelBookM3.config(bg='lightgreen', padx = 0)
labelBookM3.grid(row=12, column=0, padx=10, pady=10)

magazineIssueTitle = Entry(text = "")
magazineIssueTitle.place(x = 150, y = 100, width = 200, height = 25)
magazineIssueTitle.grid(row=12, column=1, columnspan=3, padx=2, pady=2)

#   buttons
# add magazine
buttonAddMag = Button(text = "add magazine", command = treemagaz_add )
buttonAddMag.place(x = 360, y = 60, width = 75, height = 35)
buttonAddMag.grid(row=10, column=4, columnspan=1)
#edit magazine
buttonEditMag = Button(text = "edit magazine", command = treemagaz_update )
buttonEditMag.place(x = 360, y = 40, width = 75, height = 35)
buttonEditMag.grid(row=11, column=4, columnspan=1)
#delete magazine
buttonDeleteMag = Button(text = "delete magazine", command = treemagaz_delete )
buttonDeleteMag.place(x = 360, y =20, width = 75, height = 35)
buttonDeleteMag.grid(row=12, column=4, columnspan=1)




buttonExportSQLightTomySQL = Button(text = "aSQLight to MYsql", command = exportSQLight )
buttonExportSQLightTomySQL.place(x = 360, y = 60, width = 75, height = 35)
buttonExportSQLightTomySQL.grid(row=10, column=10, columnspan=1)

buttonExportMySQLToPostgreSQL = Button(text = "mySQL to postgreSQL ", command = exportMySQL )
buttonExportMySQLToPostgreSQL.place(x = 360, y = 60, width = 75, height = 35)
buttonExportMySQLToPostgreSQL.grid(row=11, column=10, columnspan=1)

#    enter BOOK NAME
labelBook1 = Label(text="Enter book name")
labelBook1.place(x = 30, y = 40)
labelBook1.config(bg='lightgreen', padx = 0)
labelBook1.grid(row=1, column=0, padx=10, pady=10)

bookName = Entry(text = "")
bookName.place(x = 150, y =40, width = 200, height = 25)
bookName.grid(row=1, column=1, columnspan=3, padx=2, pady=2)

#    enter BOOK GENRE
labelBook2 = Label(text="Enter book genre")
labelBook2.place(x = 30, y = 70)
labelBook2.config(bg='lightgreen', padx = 0)
labelBook2.grid(row=2, column=0, padx=10, pady=10)

bookGenre = Entry(text = "")
bookGenre.place(x = 150, y =70, width = 200, height = 25)
bookGenre.grid(row=2, column=1, columnspan=3, padx=2, pady=2)

#  enter BOOK YEAR
labelBook3 = Label(text="Enter book year")
labelBook3.place(x = 30, y = 100)
labelBook3.config(bg='lightgreen', padx = 0)
labelBook3.grid(row=3, column=0, padx=10, pady=10)

bookYear = Entry(text = "")
bookYear.place(x = 150, y = 100, width = 200, height = 25)
bookYear.grid(row=3, column=1, columnspan=3, padx=2, pady=2)

# add book
buttonAdd = Button(text = "add book", command = treebook_add )
buttonAdd.place(x = 360, y = 60, width = 75, height = 35)
buttonAdd.grid(row=1, column=4, columnspan=1)
#edit book
buttonEdit = Button(text = "edit book", command = treebook_update )
buttonEdit.place(x = 360, y = 40, width = 75, height = 35)
buttonEdit.grid(row=2, column=4, columnspan=1)
#delete book
buttonDelete = Button(text = "delete book", command = treebook_delete )
buttonDelete.place(x = 360, y =20, width = 75, height = 35)
buttonDelete.grid(row=3, column=4, columnspan=1)




#-----END     GUI

window.mainloop()

