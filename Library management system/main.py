from tkinter import *
from tkinter import ttk


class Main:
    def __init__(self, master):
        self.master = master

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
        ent_search = Entry(search_bar, width=30, bd=5)
        ent_search.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
        btn_search = Button(search_bar, text='Search', font='arial 12', bg='#fcc324', fg='white')
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
        btn_list = Button(list_bar, text='List books', bg='#2488ff', fg='white', font='arial 12')
        btn_list.grid(row=1, column=3, padx=40, pady=10)

        # add book
        self.icon_book = PhotoImage(file='icons/add_book.png')
        self.btn_book = Button(top_frame, text='Add Book', image=self.icon_book, compound=LEFT, font='arial 12 bold')
        self.btn_book.pack(side=LEFT)
        # add member
        self.icon_member = PhotoImage(file='icons/users.png')
        self.btn_member = Button(top_frame, text='Add Member', font='arial 12 bold', padx=10)
        self.btn_member.configure(image=self.icon_member, compound=LEFT)
        self.btn_member.pack(side=LEFT)
        # give book
        self.icon_give = PhotoImage(file='icons/givebook.png')
        self.btn_give = Button(top_frame, text='Give Book', image=self.icon_give, compound=LEFT, font='arial 12 bold')
        self.btn_give.pack(side=LEFT)


def main():
    root = Tk()
    app = Main(root)
    root.title('Library management system')
    root.geometry('1350x650+150+50')
    root.iconbitmap('icons/icon.ico')
    root.mainloop()


if __name__ == '__main__':
    main()
