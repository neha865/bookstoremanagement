import sqlite3
import tkinter.messagebox
from tkinter import messagebox
def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()
    tkinter.messagebox.showinfo(title="insert", message="inserted")

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book ")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    a=tkinter.messagebox.askyesno(title='Delete', message='Do you want to delete?')
    if a==True:
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        tkinter.messagebox.showinfo(title="Done", message="Deleted!")
        view()
    else:
        tkinter.messagebox.showinfo(title="Unsuccessful",message='Not deleted!')

def update(id, title, author, year, isbn):
    b = tkinter.messagebox.askyesno(title='Delete', message='Do you want to delete?')
    if b == True:
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
        conn.commit()
        conn.close()
        tkinter.messagebox.showinfo(title="Update", message="Updated!")
    else:
        tkinter.messagebox.showinfo(title='no',message='The update was not done')

connect()



