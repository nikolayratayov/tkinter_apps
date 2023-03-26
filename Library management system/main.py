from tkinter import *
from tkinter import ttk
import sqlite3
import add_book, add_member


con = sqlite3.connect('library.db')
cur = con.cursor()


class Main:
    def __init__(self, master):
        self.master = master

        def display_books(self):
            books = cur.execute('SELECT * FROM books').fetchall()
            count = 0
            for book in books:
                self.list_books.insert(count, str(book[0]) + '-' + book[1])
                count += 1

            def book_info(e):
                value = str(self.list_books.get(self.list_books.curselection()))
                id = value.split('-')[0]
                book = cur.execute('SELECT * FROM books WHERE book_id=?', (id,))
                book_information = book.fetchall()
                self.list_details.delete(0, 'end')
                self.list_details.insert(0, f'Book name: {book_information[0][1]}')
                self.list_details.insert(1, f'Author: {book_information[0][2]}')
                self.list_details.insert(2, f'Pages : {book_information[0][3]}')
                self.list_details.insert(3, f'Language : {book_information[0][4]}')
                if book_information[0][5] == 0:
                    self.list_details.insert(4, 'Status : Available')
                else:
                    self.list_details.insert(4, 'Status : Taken')
            self.list_books.bind('<<ListboxSelect>>', book_info)

        # Frames
        main_frame = Frame(self.master)
        main_frame.pack()
        # top frame
        top_frame = Frame(main_frame, width=1350, height=70, bg='#f8f8f8', relief=SUNKEN, borderwidth=3)
        top_frame.pack(fill=X)
        # center frame
        center_frame = Frame(main_frame, width=1350, height=575, relief=RIDGE, bg='#e0f0f0', borderwidth=3)
        center_frame.pack()
        # center left frame
        center_left_frame = Frame(center_frame, width=900, height=575, bg='#e0f0f0', borderwidth=3, relief=SUNKEN)
        center_left_frame.pack(side=LEFT)
        # center_right_frame
        center_right_frame = Frame(center_frame, width=450, height=575, bg='#e0f0f0', borderwidth=3, relief=SUNKEN)
        center_right_frame.pack()
        # search bar
        search_bar = LabelFrame(center_right_frame, width=440, height=75, text='Search box', bg='#9bc9ff')
        search_bar.pack(fill=X)
        lbl_search = Label(search_bar, text='Search', font='aral 12 bold', bg='#9bc9ff', fg='white')
        lbl_search.grid(row=0, column=0, padx=20, pady=10)
        self.ent_search = Entry(search_bar, width=30, bd=5)
        self.ent_search.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
        btn_search = Button(search_bar, text='Search', font='arial 12', bg='#fcc324', fg='white', command=self.search_books)
        btn_search.grid(row=0, column=4, padx=20, pady=10)

        # list bar
        list_bar = LabelFrame(center_right_frame, width=440, height=175, text='List box', bg='#fcc324')
        list_bar.pack(fill=X)
        lbl_list = Label(list_bar, text='Sort by', font='times 16 bold', fg='#2488ff', bg='#fcc324')
        lbl_list.grid(row=0, column=2)
        self.list_choice = IntVar()
        rb1 = Radiobutton(list_bar, text='All books', var=self.list_choice, value=1, bg='#fcc324')
        rb2 = Radiobutton(list_bar, text='In library', var=self.list_choice, value=2, bg='#fcc324')
        rb3 = Radiobutton(list_bar, text='Borrowed books', var=self.list_choice, value=3, bg='#fcc324')
        rb1.grid(row=1, column=0)
        rb2.grid(row=1, column=1)
        rb3.grid(row=1, column=2)
        btn_list = Button(list_bar, text='List books', bg='#2488ff', fg='white', font='arial 12', command=self.func_list_books)
        btn_list.grid(row=1, column=3, padx=40, pady=10)

        # title and image
        image_bar = Frame(center_right_frame, width=440, height=350)
        image_bar.pack(fill=BOTH)
        self.title_right = Label(image_bar, text='Welcome to our library', font='arial 16 bold')
        self.title_right.grid(row=0)
        self.img_library = PhotoImage(file='icons/library.png')
        self.lbl_img = Label(image_bar, image=self.img_library)
        self.lbl_img.grid(row=1)

        # Toolbar
        # add book
        self.icon_book = PhotoImage(file='icons/add_book.png')
        self.btn_book = Button(top_frame, text='Add Book', image=self.icon_book, compound=LEFT, font='arial 12 bold',
                               command=self.add_book)
        self.btn_book.pack(side=LEFT)
        # add member
        self.icon_member = PhotoImage(file='icons/users.png')
        self.btn_member = Button(top_frame, text='Add Member', font='arial 12 bold', padx=10, command=self.add_member)
        self.btn_member.configure(image=self.icon_member, compound=LEFT)
        self.btn_member.pack(side=LEFT)
        # give book
        self.icon_give = PhotoImage(file='icons/givebook.png')
        self.btn_give = Button(top_frame, text='Give Book', image=self.icon_give, compound=LEFT, font='arial 12 bold')
        self.btn_give.pack(side=LEFT)

        # Tabs
        # Tab1
        self.tabs = ttk.Notebook(center_left_frame, width=900, height=660)
        self.tabs.pack()
        self.tab1_icon = PhotoImage(file='icons/books.png')
        self.tab2_icon = PhotoImage(file='icons/members.png')
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text='Library management', image=self.tab1_icon, compound=LEFT)
        self.tabs.add(self.tab2, text='Statistics', image=self.tab2_icon, compound=LEFT)

        # List books
        self.list_books = Listbox(self.tab1, width=40, height=25, bd=5, font='times 12 bold')
        self.sb = Scrollbar(self.tab1, orient=VERTICAL)
        self.list_books.grid(row=0, column=0, padx=(0, 0), pady=10, sticky=N)
        self.sb.config(command=self.list_books.yview)
        self.list_books.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column=0, sticky=N+S+E)
        # List details
        self.list_details = Listbox(self.tab1, width=68, height=25, bd=5, font='times 12 bold')
        self.list_details.grid(row=0, column=1, padx=(10, 0), pady=10, sticky=N)

        # Tab2
        # Statistics
        self.lbl_book_count = Label(self.tab2, text='', pady=20, font='verdana 14 bold')
        self.lbl_book_count.grid(row=0)
        self.lbl_member_count = Label(self.tab2, text='', pady=20, font='verdana 14 bold')
        self.lbl_member_count.grid(row=1, sticky=W)
        self.lbl_taken_count = Label(self.tab2, text='', pady=20, font='verdana 14 bold')
        self.lbl_taken_count.grid(row=2, sticky=W)

        # Functions
        display_books(self)

    def add_book(self):
        new_book = add_book.AddBook()

    def add_member(self):
        member = add_member.AddMember()

    def search_books(self):
        value = self.ent_search.get()
        search = cur.execute('SELECT * FROM books WHERE book_name LIKE ?', ('%' + value + '%',)).fetchall()
        self.list_books.delete(0, 'end')
        count = 0
        for book in search:
            self.list_books.insert(count, str(book[0]) + '-' + book[1])
            count += 1

    def func_list_books(self):
        value = self.list_choice.get()
        if value == 1:
            res_books = cur.execute('SELECT * FROM books').fetchall()
        elif value == 2:
            res_books = cur.execute('SELECT * FROM books WHERE book_status=?', (0,)).fetchall()
        else:
            res_books = cur.execute('SELECT * FROM books WHERE book_status=>', (1,)).fetchall()
        self.list_books.delete(0, 'end')
        counter = 0
        for book in res_books:
            self.list_books.insert(counter, str(book[0]) + '-' + book[1])
            counter += 1


def main():
    root = Tk()
    app = Main(root)
    root.title('Library management system')
    root.geometry('1350x650+150+50')
    root.iconbitmap('icons/icon.ico')
    root.mainloop()


if __name__ == '__main__':
    main()
