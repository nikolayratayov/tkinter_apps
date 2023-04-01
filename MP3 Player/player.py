from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title='Choose a song', filetypes=(('mp3 Files', '*.mp3'),))
    song = song.replace('D:/GitHub/tkinter_apps/MP3 Player/audio/', '')
    song = song.replace('.mp3', '')
    playlist_box.insert(END, song)


def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title='Choose a song', filetypes=(('mp3 Files', '*.mp3'),))
    songs = [song.replace('D:/GitHub/tkinter_apps/MP3 Player/audio/', '') for song in songs]
    songs = [song.replace('.mp3', '') for song in songs]
    for i in songs:
        playlist_box.insert(END, i)


def delete_song():
    playlist_box.delete(ANCHOR)


def delete_all_songs():
    playlist_box.delete(0, END)


root = Tk()
root.title('MP3 Player')
root.geometry('500x400+500+100')

playlist_box = Listbox(root, bg='black', fg='green', width=60, selectbackground='green', selectforeground='black')
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

my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Add Songs', menu=add_song_menu)
add_song_menu.add_command(label='Add one song to playlist', command=add_song)
add_song_menu.add_command(label='Add many song to playlist', command=add_many_songs)

remove_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Remove songs', menu=remove_song_menu)
remove_song_menu.add_command(label='Delete song from playlist', command=delete_song)
remove_song_menu.add_command(label='Delete all songs from playlist', command=delete_all_songs)


root.mainloop()