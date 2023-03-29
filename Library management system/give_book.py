from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

con = sqlite3.connect('library.db')
cur = con.cursor()

class GiveBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('550x650+550+100')
        self.title('Give Book')
        self.resizable(False, False)
        query = 'SELECT * FROM books WHERE book_status=0'
        books = cur.execute(query).fetchall()
        book_list = [str(book[0]) + '-' + book[1] for book in books]
        query2 = 'SELECT * FROM members'
        members = cur.execute(query2).fetchall()
        member_list = [str(member[0]) + '-' + member[1] for member in members]

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
        heading = Label(self.top_frame, text='   Give book ', font='arial 22 bold', fg='#003f8a', bg='white')
        heading.place(x=290, y=60)

        # Entries and labels
        # name
        self.book_name = StringVar()
        self.lbl_name = Label(self.bottom_frame, text='Book Name', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.combo_name = ttk.Combobox(self.bottom_frame, textvariable=self.book_name)
        self.combo_name['values'] = book_list
        self.combo_name.place(x=190, y=45)

        # phone
        self.member_name = StringVar()
        self.lbl_phone = Label(self.bottom_frame, text='Member Name', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40, y=80)
        self.combo_member = ttk.Combobox(self.bottom_frame, textvariable=self.member_name)
        self.combo_member['values'] = member_list
        self.combo_member.place(x=190, y=85)

        # Button
        button = Button(self.bottom_frame, text='Give book', command=self.lend_book)
        button.place(x=255, y=120)

    def lend_book(self):
        book_name = self.book_name.get()
        member_name = self.member_name.get()
        self.book_id = book_name.split('-')[0]
        if book_name and member_name:
            try:
                query = 'INSERT INTO borrows (bor_book_id, bor_member_id) VALUES(?, ?)'
                cur.execute(query, (book_name, member_name))
                con.commit()
                messagebox.showinfo('Succes', 'Success!')
                cur.execute('UPDATE books SET book_status=? WHERE book_id=?', (1, self.book_id))
                con.commit()
            except:
                messagebox.showerror('Error', 'Something went wrong!')
        else:
            messagebox.showerror('Error', 'Fields can\'t be empty!')