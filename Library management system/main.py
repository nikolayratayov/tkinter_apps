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
        top_frame.pack()
        # center frame
        center_frame = Frame(main_frame, width=1350, height=575, relief=RIDGE, bg='#e0f0f0', borderwidth=3)
        center_frame.pack()
        # center left frame
        center_left_frame = Frame(center_frame, width=900, height=575, bg='#e0f0f0', borderwidth=3, relief=SUNKEN)
        center_left_frame.pack(side=LEFT)
        # center_right_frame
        center_right_frame = Frame(center_frame, width=450, height=575, bg='#e0f0f0', borderwidth=3, relief=SUNKEN)
        center_right_frame.pack()


def main():
    root = Tk()
    app = Main(root)
    root.title('Library management system')
    root.geometry('1350x650+150+50')
    root.iconbitmap('icons/icon.ico')
    root.mainloop()


if __name__ == '__main__':
    main()
