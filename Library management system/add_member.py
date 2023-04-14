from tkinter import *
from tkinter import messagebox
import sqlite3


con = sqlite3.connect('library.db')
cur = con.cursor()


class AddMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x650+550+100')
        self.title('Add member')

        # Frames
        # Top Frame
        self.top_frame = Frame(self, height=150, bg='white')
        self.top_frame.pack(fill=X)
        # Bottom frame
        self.bottom_frame = Frame(self, height=500, bg='#fcc324')
        self.bottom_frame.pack(fill=X)
        # Heading, image
        self.top_image = PhotoImage(file='icons/addperson.png')
        top_image_lbl = Label(self.top_frame, image=self.top_image, bg='white')
        top_image_lbl.place(x=120, y=10)
        heading = Label(self.top_frame, text='   Add member ', font='arial 22 bold', fg='#003f8a', bg='white')
        heading.place(x=290, y=60)

        # Entries and labels
        # name
        self.lbl_name = Label(self.bottom_frame, text='Name', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.ent_name = Entry(self.bottom_frame, width=30, bd=4)
        self.ent_name.place(x=150, y=45)
        # phone
        self.lbl_phone = Label(self.bottom_frame, text='Author', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40, y=80)
        self.ent_phone = Entry(self.bottom_frame, width=30, bd=4)
        self.ent_phone.place(x=150, y=85)
        # Button
        button = Button(self.bottom_frame, text='Add member', command=self.add)
        button.place(x=255, y=120)

    def add(self):
        name = self.ent_name.get()
        phone = self.ent_phone.get()
        if name and phone:
            try:
                query = 'INSERT INTO members (member_name, member_phone) VALUES(?,?)'
                cur.execute(query, (name, phone))
                con.commit()
                messagebox.showinfo('Success', 'Successfully added to database!', icon='info')
            except:
                messagebox.showerror('Error', 'Can\'t add to database!')
        else:
            messagebox.showerror('Error', 'Fields can\'t be empty!')
