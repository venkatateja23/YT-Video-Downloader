#Use 'pip install pytube' in terminal first to install pytube library
#from pytube library import YouTube
#import tkinter module for GUI
from pytube import YouTube
from tkinter import *


#Create a function to download videos from YT
def download():
    youtubeObject = YouTube(str(link.get()))#captures link of the video and locates it in YouTube  
    youtubeObject = youtubeObject.streams.get_highest_resolution()#downloads highest available resolution
    #to handle exceptions
    try:
        youtubeObject.download("C:\\Users\\91912\\OneDrive\\Desktop\\YT-Video-Downloader\\Result")#location to save downloaded videos
    except:
        #returns an error message if download failed
        Label(win, text="Error Occurred", font="arial 15", fg="Red").place(x=150, y=240)
    #returns download success message after successful completion
    Label(win, text="Downloaded Successfully", font="arial 15", fg="Green").place(x=150, y=240)


#For Graphical User Interface(GUI)
win = Tk()
win.geometry("500x300")
win.resizable(0, 0)
win.title("YouTube Video Downloader")
Label(win, text="Paste your link here:", fg="Purple", font="san-serif 15 bold").place(x=150, y=55)
link = StringVar()
linkEntry = Entry(win, textvariable=link, width=50)
linkEntry.place(x=100, y=90)

Button(win, text="Download", font="san-serif 16 bold", bg="RoyalBlue2", fg="Black", command=download).place(x=190, y=180)

win.mainloop()
