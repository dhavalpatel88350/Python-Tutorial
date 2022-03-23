import sqlite3 
def connection():
    a=sqlite3.connect('mydatabase.db')
    return a

def create(a):
    b=a.execute("CREATE TABLE STUDENT(NAME TEXT,AGE INTEGER)")

# def insert(a):
#     name=input("enter name")
#     age=int(input("enter age:"))
#     V=a.execute("INSERT INTO STUDENT(NAME,AGE) VALUES(?,?)",(name,age))

# obj=connection()
# insert(obj)
# obj.commit()
# obj.close()