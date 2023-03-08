from tkinter import *
import sqlite3


con = sqlite3.connect('database.db')
cur = con.cursor()


class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x650+520+100')
        self.title('My People')
        self.resizable(False, False)
