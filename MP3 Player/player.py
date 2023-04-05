from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pygame
import time
from mutagen.mp3 import MP3


pygame.mixer.init()


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


def play():
    song = playlist_box.get(playlist_box.curselection())
    song = f'D:/GitHub/tkinter_apps/MP3 Player/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    play_time()


def stop():
    pygame.mixer.music.stop()
    status_bar.config(text=f'')


def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        paused = False
        pygame.mixer.music.unpause()
    else:
        paused = True
        pygame.mixer.music.pause()


def next_song():
    next = playlist_box.curselection()
    if next:
        next = next[0] + 1
        if next == playlist_box.size():
            next = 0
    else:
        next = 0
    playlist_box.selection_clear(0, END)
    playlist_box.selection_set(next)
    play()


def previous_song():
    previous = playlist_box.curselection()
    if previous:
        previous = previous[0] - 1
        if previous == -1:
            previous = playlist_box.size() - 1
    else:
        previous = playlist_box.size() - 1
    playlist_box.selection_clear(0, END)
    playlist_box.selection_set(previous)
    play()


def play_time():
    current_time = pygame.mixer.music.get_pos() / 1000
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))
    song = playlist_box.get(playlist_box.curselection())
    song = f'D:/GitHub/tkinter_apps/MP3 Player/audio/{song}.mp3'
    song_mut = MP3(song)
    global song_length
    song_length = song_mut.info.length
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))
    if current_time >= 1:
        status_bar.config(text=f'Time elapsed: {converted_current_time} of {converted_song_length}  ')
    status_bar.after(1000, play_time)


def volume(x):
    pygame.mixer.music.set_volume(volume_slide.get())


paused = False

root = Tk()
root.title('MP3 Player')
root.geometry('500x400+500+100')

main_frame = ttk.Frame(root)
main_frame.pack(pady=20)

playlist_box = Listbox(main_frame, bg='black', fg='green', width=60, selectbackground='green', selectforeground='black')
playlist_box.grid(row=0, column=0)

volume_frame = ttk.LabelFrame(main_frame, text='Volume')
volume_frame.grid(row=0, column=1, padx=10)
volume_slide = ttk.Scale(volume_frame, from_=1, to=0, orient=VERTICAL, length=125, command=volume, value=1)
volume_slide.pack(pady=10)

control_frame = ttk.Frame(main_frame)
control_frame.grid(row=1, column=0, pady=20)

back_image = PhotoImage(file='images/back50.png')
forward_image = PhotoImage(file='images/forward50.png')
play_image = PhotoImage(file='images/play50.png')
pause_image = PhotoImage(file='images/pause50.png')
stop_image = PhotoImage(file='images/stop50.png')


back_button = ttk.Button(control_frame, image=back_image, command=previous_song)
back_button.grid(row=0, column=0, padx=10)
forward_button = ttk.Button(control_frame, image=forward_image, command=next_song)
forward_button.grid(row=0, column=1, padx=10)
play_button = ttk.Button(control_frame, image=play_image, command=play)
play_button.grid(row=0, column=2, padx=10)
pause_button = ttk.Button(control_frame, image=pause_image, command=lambda: pause(paused))
pause_button.grid(row=0, column=3, padx=10)
stop_button = ttk.Button(control_frame, image=stop_image, command=stop)
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

status_bar = ttk.Label(root, text='', border=1, relief=GROOVE, anchor=E)
status_bar.pack(fil=X, side=BOTTOM, ipady=2)


root.mainloop()