from tkinter import *
import sqlite3
import addperson


con = sqlite3.connect('database.db')
cur = con.cursor()


class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x650+520+100')
        self.title('My People')
        self.resizable(False, False)

        # Frames
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=500, bg='#fcc324')
        self.bottom.pack(fill=X)

        # Heading, image and date
        self.top_image = PhotoImage(file='icons/person_icon.png')
        self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y=10)
        self.heading = Label(self.top, text='My People', font='arial 15 bold', fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)

        # scrollbar
        self.sb = Scrollbar(self.bottom, orient=VERTICAL)

        # listbox
        self.list_box = Listbox(self.bottom, width=60, height=31)
        self.list_box.grid(row=0, column=0, padx=(40, 0))
        self.sb.config(command=self.list_box.yview)
        self.list_box.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column=1, sticky=N+S)

        # Buttons
        btn_add = Button(self.bottom, text='Add', width=12, font='Sans 12 bold', command=self.add_person)
        btn_add.grid(row=0, column=2, sticky=N, padx=10, pady=10)

        btn_update = Button(self.bottom, text='Update', width=12, font='Sans 12 bold')
        btn_update.grid(row=0, column=2, sticky=N, padx=10, pady=50)

        btn_display = Button(self.bottom, text='Display', width=12, font='Sans 12 bold')
        btn_display.grid(row=0, column=2, sticky=N, padx=10, pady=90)

        btn_delete = Button(self.bottom, text='Delete', width=12, font='Sans 12 bold')
        btn_delete.grid(row=0, column=2, sticky=N, padx=10, pady=130)

    def add_person(self):
        add_page = addperson.AddPerson()
