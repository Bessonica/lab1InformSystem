import psycopg2

# tables books1, magazines1

#    create table
# cur.execute("CREATE TABLE test (id SERIAL PRIMARY KEY, name VARCHAR);")
# pSQLconn.commit()
# cur.execute("CREATE TABLE books1 (id SERIAL PRIMARY KEY, name VARCHAR, year VARCHAR);")
# pSQLconn.commit()
# cur.execute("CREATE TABLE magazines1 (id SERIAL PRIMARY KEY, title VARCHAR, issue VARCHAR);")
# pSQLconn.commit()

#    insert data into table
# cur.execute("INSERT INTO test (name) VALUES(%s)", ("one",))
# pSQLconn.commit()


hostname = "localhost"
database = "test"
username = "postgres"
pwd = "agoptq"
port_id = 5432

pSQLconn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    password = pwd,
    port = port_id
)

cur = pSQLconn.cursor()

# cur.execute("INSERT INTO magazines1 (title, issue) VALUES(%s, %s)", ("three", "four", ))
# pSQLconn.commit()

cur.execute("SELECT * FROM magazines1")
tables = cur.fetchall()
print("select all from test")
for table in tables:
    print(table)

class dataBasePostg:
    def __init__(self):
        self.pSQLconn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id
        )

        self.cur = self.pSQLconn.cursor()

    def show(self):
        self.cur.execute("SELECT * FROM magazines1")
        self.tables = self.cur.fetchall()
        print("POSTGR SQL: select all from magazines1")
        for table in self.tables:
            print(table)

        self.cur.execute("SELECT * FROM books1")
        self.tables = self.cur.fetchall()
        print("POSTGR SQL: select all from books1")
        for table in self.tables:
            print(table)

    def showBooks(self):
        self.cur.execute("SELECT * FROM books1")
        self.rows = self.cur.fetchall()
        return self.rows

    def showMagazines(self):
        self.cur.execute("SELECT * FROM magazines1")
        self.rows = self.cur.fetchall()
        return self.rows
       



        
newCur = dataBasePostg()
newCur.showMagazines()
print(newCur.showMagazines())

#    create table
# cur.execute("CREATE TABLE test (id SERIAL PRIMARY KEY, name VARCHAR);")
# pSQLconn.commit()
#    insert data into table
# cur.execute("INSERT INTO test (name) VALUES(%s)", ("one",))
# pSQLconn.commit()

# cur.execute("SELECT * FROM test")
# print(cur.fetchall())

cur.close()
pSQLconn.close()