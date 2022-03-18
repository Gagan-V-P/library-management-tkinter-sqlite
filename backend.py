import sqlite3

def connect():
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title TEXT,author text, year integer,isbn integer)")
    conn.commit()
    conn.close()

def insert(tl,atr,year,isbn):
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?) ", (tl,atr,year,isbn))
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    # conn.commit()
    rows=cur.fetchall()
    conn.close()
    return rows

def search(tl="",atr="",year="",isbn=""): # empty string to ensure only one information can be given
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(tl,atr,year,isbn))
    # conn.commit()
    rows=cur.fetchall()
    conn.close()
    return rows
    
def delete(id):
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,)) # comma bcoz it should be in tuple form
    conn.commit()
    conn.close()
    
def update(id,tl,atr,year,isbn):
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? where id=?",(tl,atr,year,isbn,id))
    conn.commit()
    conn.close()

connect()
# insert("the fire","jhonny",2015,462075593)
# delete(1)
# update(2,"the ice","gagan",2021,897537)
# print(view())
# print(search(atr="jhonny"))