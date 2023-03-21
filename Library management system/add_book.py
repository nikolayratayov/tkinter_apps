from tkinter import *
from tkinter import messagebox
import sqlite3


class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x650+550+100')
        self.title('Add book')

        # Frames
        # Top Frame
        self.top_frame = Frame(self, height=150, bg='white')
        self.top_frame.pack(fill=X)
        # Bottom frame
        self.bottom_frame = Frame(self, height=500, bg='#fcc324')
        self.bottom_frame.pack(fill=X)
        # Heading, image
        self.top_image = PhotoImage(file='icons/addbook.png')
        top_image_lbl = Label(self.top_frame, image=self.top_image, bg='white')
        top_image_lbl.place(x=120, y=10)
        heading = Label(self.top_frame, text='   Add book ', font='arial 22 bold', fg='#003f8a', bg='white')
        heading.place(x=290, y=60)

        # Entries and labels
        # name
        self.lbl_name = Label(self.bottom_frame, text='Name', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.ent_name = Entry(self.bottom_frame, width=30, bd=4)
        self.ent_name.place(x=150, y=45)
        # author
        self.lbl_author = Label(self.bottom_frame, text='Author', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_author.place(x=40, y=80)
        self.ent_author = Entry(self.bottom_frame, width=30, bd=4)
        self.ent_author.place(x=150, y=85)
        # page
        self.lbl_page = Label(self.bottom_frame, text='Page', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_page.place(x=40, y=120)
        self.ent_page = Entry(self.bottom_frame, width=30, bd=4)
        self.ent_page.place(x=150, y=125)
        # language
        self.lbl_language = Label(self.bottom_frame, text='Language', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_language.place(x=40, y=160)
        self.ent_language = Entry(self.bottom_frame, width=30, bd=4)
        self.ent_language.place(x=150, y=165)
        # Button
        button = Button(self.bottom_frame, text='Add book', command=self.add)
        button.place(x=270, y=200)

    def add(self):
        pass