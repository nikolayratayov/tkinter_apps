from tkinter import *


ops = ['+', '-', '*', '/']


def enter_number(x):
    if entry_box.get() == 'O':
        entry_box.delete(0, 'end')
        entry_box.insert(0, str(x))
    else:
        length = len(entry_box.get())
        entry_box.insert(length, str(x))


def enter_operator(x):
    if entry_box.get() != 'O':
        length = len(entry_box.get())
        if entry_box.get()[-1] in ops:
            entry_box.delete(length - 1)
        entry_box.insert(length, btn_operator[x]['text'])


def clear():
    entry_box.delete(0, END)
    entry_box.insert(0, 'O')


res_list = []


def result():
    if entry_box.get()[-1] in ops:
        entry_box.delete(len(entry_box.get()) - 1)
    content = entry_box.get()
    res = eval(content)
    entry_box.delete(0, END)
    entry_box.insert(0, str(res))
    res_list.append(content)
    res_list.reverse()
    status_bar.configure(text='History: ' + ' | '.join(res_list[:5]), font='verdana 10 bold')


def func_delete():
    length = len(entry_box.get())
    entry_box.delete(length - 1, 'end')
    if length == 1:
        entry_box.insert(0, 'O')


root = Tk()
root.title('Calculator')
root.geometry('380x550+850+100')
root.resizable(False, False)

entry_box = Entry(font='verdana 14 bold', width=22, bd=10, justify=RIGHT, bg='#e6e6fa')
entry_box.insert(0, 'O')
entry_box.place(x=20, y=10)

btn_numbers = []
for i in range(10):
    btn_numbers.append(Button(width=4, text=str(i), font='times 15 bold', bd=5, command=lambda x=i:enter_number(x)))

btn_text = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn_numbers[btn_text].place(x=25 + j * 90, y=70 + i * 70)
        btn_text += 1


btn_operator = []
for i in range(4):
    btn_operator.append(Button(width=4, font='times 15 bold', bd=5, command=lambda x=i:enter_operator(x)))

btn_operator[0]['text'] = '+'
btn_operator[1]['text'] = '-'
btn_operator[2]['text'] = '*'
btn_operator[3]['text'] = '/'

for i in range(4):
    btn_operator[i].place(x=290, y=70 + i * 70)

btn_zero = Button(width=19, text='0', font='times 15 bold', bd=5, command=lambda x=0: enter_number(x))
btn_clear = Button(width=4, text='C', font='times 15 bold', bd=5, command=clear)
btn_zero.place(x=25, y=280)
btn_clear.place(x=25, y=340)
btn_dot = Button(width=4, text='.', font='times 15 bold', bd=5, command=lambda x='.': enter_number(x))
btn_dot.place(x=110, y=340)
btn_equal = Button(width=4, text='=', font='times 15 bold', bd=5, command=result)
btn_equal.place(x=200, y=340)
icon = PhotoImage(file='icons/arrow.png')
btn_delete = Button(width=50, height=35, font='times 15 bold', bd=5, command=func_delete, image=icon)
btn_delete.place(x=290, y=340)

status_bar = Label(root, text='History: ', relief=SUNKEN, height=3, anchor=W, font='verdana 11 bold')
status_bar.pack(side=BOTTOM, fill=X)

root.mainloop()
