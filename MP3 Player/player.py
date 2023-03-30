from tkinter import *
from tkinter import ttk


root = Tk()
root.title('MP3 Player')
root.geometry('500x400+500+100')

playlist_box = Listbox(root, bg='black', fg='green', width=60)
playlist_box.pack(pady=20)

control_frame = ttk.Frame(root)
control_frame.pack(pady=20)

back_image = PhotoImage(file='images/back50.png')
forward_image = PhotoImage(file='images/forward50.png')
play_image = PhotoImage(file='images/play50.png')
pause_image = PhotoImage(file='images/pause50.png')
stop_image = PhotoImage(file='images/stop50.png')


back_button = ttk.Button(control_frame, image=back_image)
back_button.grid(row=0, column=0, padx=10)
forward_button = ttk.Button(control_frame, image=forward_image)
forward_button.grid(row=0, column=1, padx=10)
play_button = ttk.Button(control_frame, image=play_image)
play_button.grid(row=0, column=2, padx=10)
pause_button = ttk.Button(control_frame, image=pause_image)
pause_button.grid(row=0, column=3, padx=10)
stop_button = ttk.Button(control_frame, image=stop_image)
stop_button.grid(row=0, column=4, padx=10)

root.mainloop()