import pytube
import os
import tkinter as tk

root = tk.Tk()
text1 = tk.Entry(root, width=50)
name1 = tk.Entry(root, width=50)
label = tk.Label(root, text="Youtube Video Downloader")
label.pack()
name1.insert(0, "Enter Name of Video")
text1.insert(0, "Enter Link")
name1.pack()
text1.pack()
def download():
    link = input("Enter the youtube link you want to donwload: ")
    name = input("Name the vidoe: ")
    yt = pytube.YouTube(link)
    if yt.views >= 1000000:
        if path.exists('overmil'):
            stream = yt.streams.get_highest_resolution()
            stream.download('overmil')
            video_name = stream.default_filename
            os.rename(video_name, name + ".mp4")
        else:
            os.mkdir('overmil')
            stream = yt.streams.get_highest_resolution()
            stream.download('overmil')
            video_name = stream.default_filename
            os.rename(video_name, name + ".mp4")
    else:
        if path.exists('undermil'):
            print("This video has less than million views, it's in undermil")
            stream = yt.streams.get_highest_resolution()
            stream.download('undermil')
            video_name = stream.default_filename
            os.rename(video_name, name + ".mp4")
        else:
            os.mkdir('undermil')
            print("This video has less than million views, it's in undermil")
            stream = yt.streams.get_highest_resolution()
            stream.download('undermil')
            video_name = stream.default_filename
            os.rename(video_name, name + ".mp4")

downloadButton = tk.Button(root, text="Download", fg="white", bg="#263D42", command=download1)
downloadButton.pack()



root.mainloop()



