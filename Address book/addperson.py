from tkinter import *
import sqlite3


con = sqlite3.connect('database.db')
cur = con.cursor()


class AddPerson(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x750+550+100')
        self.title('Add Person')
        self.resizable(False, False)

        # Frames
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=500, bg='#fcc324')
        self.bottom.pack(fill=X)

        # Heading, image and date
        self.top_image = PhotoImage(file='icons/addperson.png')
        self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y=10)
        self.heading = Label(self.top, text='My People', font='arial 15 bold', fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)

        # Labels and entries
        self.lbl_name = Label(self.bottom, text='Name', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.ent_name = Entry(self.bottom, width=30, bd=4)
        self.ent_name.insert(0, 'Please enter a name')
        self.ent_name.place(x=150, y=45)

        self.lbl_surname = Label(self.bottom, text='Surname', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_surname.place(x=40, y=80)
        self.ent_surname = Entry(self.bottom, width=30, bd=4)
        self.ent_surname.insert(0, 'Please enter a surname')
        self.ent_surname.place(x=150, y=85)

        self.lbl_email = Label(self.bottom, text='Email', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_email.place(x=40, y=120)
        self.ent_email = Entry(self.bottom, width=30, bd=4)
        self.ent_email.insert(0, 'Please enter an email')
        self.ent_email.place(x=150, y=125)

        self.lbl_phone = Label(self.bottom, text='Phone', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40, y=160)
        self.ent_phone = Entry(self.bottom, width=30, bd=4)
        self.ent_phone.insert(0, 'Please enter a phone number')
        self.ent_phone.place(x=150, y=165)

        self.lbl_address = Label(self.bottom, text='Address', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_address.place(x=40, y=300)
        self.address = Text(self.bottom, width=23, height=15, wrap=WORD)
        self.address.place(x=150, y=200)

        button = Button(self.bottom, text='Add person')
        button.place(x=270, y=460)