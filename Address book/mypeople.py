from tkinter import *
import sqlite3
import addperson
from tkinter import messagebox


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

        people = cur.execute("SELECT * FROM people").fetchall()
        counter = 0
        for person in people:
            self.list_box.insert(counter, str(person[0]) + '-' + person[1] + ' ' + person[2])
            counter += 1

        # Buttons
        btn_add = Button(self.bottom, text='Add', width=12, font='Sans 12 bold', command=self.add_person)
        btn_add.grid(row=0, column=2, sticky=N, padx=10, pady=10)

        btn_update = Button(self.bottom, text='Update', width=12, font='Sans 12 bold', command=self.update)
        btn_update.grid(row=0, column=2, sticky=N, padx=10, pady=50)

        btn_display = Button(self.bottom, text='Display', width=12, font='Sans 12 bold', command=self.display)
        btn_display.grid(row=0, column=2, sticky=N, padx=10, pady=90)

        btn_delete = Button(self.bottom, text='Delete', width=12, font='Sans 12 bold')
        btn_delete.grid(row=0, column=2, sticky=N, padx=10, pady=130)

    def add_person(self):
        add_page = addperson.AddPerson()
        self.destroy()

    def update(self):
        global person_id
        selected_item = self.list_box.curselection()
        person = self.list_box.get(selected_item)
        person_id = person.split('-')[0]
        update_page = Update()

    def display(self):
        global person_id
        selected_item = self.list_box.curselection()
        person = self.list_box.get(selected_item)
        person_id = person.split('-')[0]
        display_page = Display()
        self.destroy()


class Update(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x650+550+100')
        self.title('Update person')
        self.resizable(False, False)

        # get person from db
        person = cur.execute("SELECT * from people WHERE person_id =?", (person_id,))
        person_info = person.fetchall()
        self.person_id = person_info[0][0]
        self.person_name = person_info[0][1]
        self.person_surname = person_info[0][2]
        self.person_email = person_info[0][3]
        self.person_phone = person_info[0][4]
        self.person_address = person_info[0][5]

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
        self.ent_name.insert(0, self.person_name)
        self.ent_name.place(x=150, y=45)

        self.lbl_surname = Label(self.bottom, text='Surname', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_surname.place(x=40, y=80)
        self.ent_surname = Entry(self.bottom, width=30, bd=4)
        self.ent_surname.insert(0, self.person_surname)
        self.ent_surname.place(x=150, y=85)

        self.lbl_email = Label(self.bottom, text='Email', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_email.place(x=40, y=120)
        self.ent_email = Entry(self.bottom, width=30, bd=4)
        self.ent_email.insert(0, self.person_email)
        self.ent_email.place(x=150, y=125)

        self.lbl_phone = Label(self.bottom, text='Phone', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40, y=160)
        self.ent_phone = Entry(self.bottom, width=30, bd=4)
        self.ent_phone.insert(0, self.person_phone)
        self.ent_phone.place(x=150, y=165)

        self.lbl_address = Label(self.bottom, text='Address', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_address.place(x=40, y=300)
        self.address = Text(self.bottom, width=23, height=15, wrap=WORD)
        self.address.insert('1.0', self.person_address)
        self.address.place(x=150, y=200)

        button = Button(self.bottom, text='Update person', command=self.update_person)
        button.place(x=270, y=460)

    def update_person(self):
        person_id = self.person_id
        person_name = self.ent_name.get()
        person_surname = self.ent_surname.get()
        person_email = self.ent_email.get()
        person_phone = self.ent_phone.get()
        person_address = self.address.get(1.0, 'end-1c')

        if person_name and person_surname and person_email and person_phone and person_address:
            try:
                query = "UPDATE people set person_name=?, person_surname=?, person_email=?, person_phone=?, person_address=?" \
                        " WHERE person_id=?"
                cur.execute(query, (person_name, person_surname, person_email, person_phone, person_address, person_id))
                con.commit()
                messagebox.showinfo('Success', 'Person has been updated!')
                self.destroy()
            except:
                messagebox.showinfo('Warning', 'Person has not been updated!', icon='warning')
        else:
            messagebox.showinfo('Warning', 'Fields can\'t be empty!', icon='warning')


class Display(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x650+550+100')
        self.title('Display Person')
        self.resizable(False, False)

        person = cur.execute("SELECT * from people WHERE person_id =?", (person_id,))
        person_info = person.fetchall()
        self.person_id = person_info[0][0]
        self.person_name = person_info[0][1]
        self.person_surname = person_info[0][2]
        self.person_email = person_info[0][3]
        self.person_phone = person_info[0][4]
        self.person_address = person_info[0][5]

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
        self.ent_name.insert(0, self.person_name)
        self.ent_name.config(state='disabled')
        self.ent_name.place(x=150, y=45)

        self.lbl_surname = Label(self.bottom, text='Surname', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_surname.place(x=40, y=80)
        self.ent_surname = Entry(self.bottom, width=30, bd=4)
        self.ent_surname.insert(0, self.person_surname)
        self.ent_surname.config(state='disabled')
        self.ent_surname.place(x=150, y=85)

        self.lbl_email = Label(self.bottom, text='Email', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_email.place(x=40, y=120)
        self.ent_email = Entry(self.bottom, width=30, bd=4)
        self.ent_email.insert(0, self.person_email)
        self.ent_email.config(state='disabled')
        self.ent_email.place(x=150, y=125)

        self.lbl_phone = Label(self.bottom, text='Phone', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40, y=160)
        self.ent_phone = Entry(self.bottom, width=30, bd=4)
        self.ent_phone.insert(0, self.person_phone)
        self.ent_phone.config(state='disabled')
        self.ent_phone.place(x=150, y=165)

        self.lbl_address = Label(self.bottom, text='Address', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_address.place(x=40, y=300)
        self.address = Text(self.bottom, width=23, height=15, wrap=WORD)
        self.address.insert('1.0', self.person_address)
        self.address.config(state='disabled')
        self.address.place(x=150, y=200)
