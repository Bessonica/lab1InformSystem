from select import select
from tkinter import *
from tkinter import ttk



class windowTK:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1200x720")
        self.tree = ttk.Treeview(self.window)

        

        # self.tree = ttk.Treeview(self.window)

        # self.tree['columns'] = ("ID", "Title", "Genre", "Year")

        # self.tree.column("#0", width=0, stretch=NO)
        # self.tree.column("ID", anchor=W, width=100)
        # self.tree.column("Title", anchor=W, width=200)
        # self.tree.column("Genre", anchor=W, width=150)
        # self.tree.column("Year", anchor=W, width=150)

        # self.tree.heading("ID", text="ID", anchor=W)
        # self.tree.heading("Title", text="Title", anchor=W)
        # self.tree.heading("Genre", text="Genre", anchor=W)
        # self.tree.heading("Year", text="Year", anchor=W)

        # self.tree.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 15))
        # self.tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)


        

# def setUpLabels():
#     labelBookM1 = Label(text="Enter magazine title")
#     labelBookM1.place(x = 30, y = 40)
#     labelBookM1.config(bg='lightgreen', padx = 0)
#     labelBookM1.grid(row=10, column=0, padx=10, pady=10)

#     magazineName = Entry(text = "")
#     magazineName.place(x = 150, y =40, width = 200, height = 25)
#     magazineName.grid(row= 10, column=1, columnspan=3, padx=2, pady=2)

#     return


# labelBookM2 = Label(text="Enter magazine issue")
# labelBookM2.place(x = 30, y = 70)
# labelBookM2.config(bg='lightgreen', padx = 0)
# labelBookM2.grid(row=11, column=0, padx=10, pady=10)

# magazineIssue = Entry(text = "")
# magazineIssue.place(x = 150, y =70, width = 200, height = 25)
# magazineIssue.grid(row=11, column=1, columnspan=3, padx=2, pady=2)

# labelBookM3 = Label(text="Enter issue title")
# labelBookM3.place(x = 30, y = 100)
# labelBookM3.config(bg='lightgreen', padx = 0)
# labelBookM3.grid(row=12, column=0, padx=10, pady=10)

# magazineIssueTitle = Entry(text = "")
# magazineIssueTitle.place(x = 150, y = 100, width = 200, height = 25)
# magazineIssueTitle.grid(row=12, column=1, columnspan=3, padx=2, pady=2)
    
