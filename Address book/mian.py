from tkinter import *
import datetime


date = datetime.datetime.now()


class Application(object):
    def __init__(self, master):
        self.master = master

        # Frames
        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(master, height=500, bg='#adff2f')
        self.bottom.pack(fill=X)

        # Heading, image and date
        self.top_image = PhotoImage(file='icons/book.png')
        self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y=10)
        self.heading = Label(self.top, text='My address book app', font='arial 15 bold', fg='#ffa500', bg='white')
        self.heading.place(x=260, y=60)
        self.date_lbl = Label(self.top, text='Today\'s date: ' + str(date), font='arial 12 bold', bg='white', fg='#ffa500')
        self.date_lbl.place(x=450, y=5)


def main():
    root = Tk()
    app = Application(root)
    root.title('Address Book')
    root.geometry('650x550+350+100')
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()