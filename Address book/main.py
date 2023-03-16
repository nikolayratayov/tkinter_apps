from tkinter import *
import mypeople, addperson, about
import datetime



date = datetime.datetime.now()


class Application:
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

        # First Button
        self.btn1_icon = PhotoImage(file='icons/man.png')
        self.person_btn = Button(self.bottom, text='   My people    ', font='arial 12 bold', command=self.open_my_people)
        self.person_btn.config(image=self.btn1_icon, compound=LEFT)
        self.person_btn.place(x=250, y=10)

        # Second Button
        self.btn2_icon = PhotoImage(file='icons/add.png')
        self.add_person_btn = Button(self.bottom, text='  Add Person  ', font='arial 12 bold', command=self.add_person)
        self.add_person_btn.config(image=self.btn2_icon, compound=LEFT)
        self.add_person_btn.place(x=250, y=70)

        # Third Button
        self.btn3_icon = PhotoImage(file='icons/info.png')
        self.about_btn = Button(self.bottom, text='  About us       ', font='arial 12 bold', command=about.main)
        self.about_btn.config(image=self.btn3_icon, compound=LEFT)
        self.about_btn.place(x=250, y=130)

    def open_my_people(self):
        people = mypeople.MyPeople()

    def add_person(self):
        add_person_window = addperson.AddPerson()


def main():
    root = Tk()
    app = Application(root)
    root.title('Address Book')
    root.geometry('650x550+350+100')
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()