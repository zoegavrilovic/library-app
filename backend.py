import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title,author,year,isbn))  #null because id is auto incrementing
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):  #empty strings so that when only one arg is given
    #we don't get an error because the others are not given
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title,author,year,isbn,id))
    conn.commit()
    conn.close()


connect()
#insert("The Sun", "John Smith", 1918, 92188474574)
#delete(3)
#update(4,"The Moon", "John Smooth", 1917, 43747893475346)
#print(view())
#print(search(author = "John Smooth"))
