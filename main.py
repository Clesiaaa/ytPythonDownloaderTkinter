from pytube import YouTube
from tkinter import *
import os

def download_mp3(link:str, output:str):
    yt = YouTube(link)
    audio_stream = yt.streams.filter(only_audio=True).first()

    output_path = output
    audio_file = audio_stream.download(output_path=output_path)

    base,ext = os.path.splitext(audio_file)
    new_file = base + '.mp3'
    
    os.rename(audio_file, new_file)


def download_mp4(link:str, output:str):
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=False).first()

    output_path = output
    out_file = video.download(output_path=output_path)

    base = os.path.splitext(out_file)
    new_file = base + '.mp4'

    os.rename(out_file, new_file)

root = Tk()
root.geometry("265x300")
root.title("Youtube downloader")

label = Label(root, text="Youtube Downloader")
entry_link = Entry(root, width=40)  
entry_output = Entry(root, width=40) 

btn_download_mp3 = Button(root, text="Download MP3", command=lambda: download_mp3(entry_link.get(), entry_output.get()))
btn_download_mp4 = Button(root, text="Download MP4", command=lambda: download_mp4(entry_link.get(), entry_output.get()))

label.grid(row=0, column=0, columnspan=2, pady=10)
entry_link.grid(row=1, column=0, padx=10, pady=10)
entry_output.grid(row=2, column=0, padx=10, pady=10)
btn_download_mp3.grid(row=3, column=0, pady=10)
btn_download_mp4.grid(row=4, column=0, pady=10)

root.mainloop()
