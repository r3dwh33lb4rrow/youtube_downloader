import tkinter
from tkinter import *
from tkinter import messagebox
from pytube import YouTube

# Set the variable prefix
gui = Tk()

# Set title for window
gui.title("YouTube Downloader")
# Set window size/geometry
gui.geometry("300x250")
# Set a background colour
gui.configure(bg="#303536")
# Set icon in window title
try:
    gui.iconbitmap("./favicon.ico")
except:
    None

# Set the label for the URL input
label = Label(gui,text="Enter the YouTube link:", bg="#303536", fg="white", font=("Helvetica", 12))
label.pack(side=TOP, pady=10)

# Create the url_entry field
url_entry = Entry(gui, font=("Helvetica", 12))
url_entry.pack(pady=10)

yt = None

# Define the input update function
def get_url():
    global yt
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL before clicking Submit.")
        return
    # Create a YouTube object
    yt = YouTube(url)

# Give the Submit and Clear buttons something to attach to, instaed of the gui itself
button_frame = Frame(gui, bg="#303536")
button_frame.pack(anchor=CENTER)

# Create the sumbit button to update the input variable url_entry
submit_button = Button(button_frame, text="Submit", command=get_url, bg="green", fg="white", font=("Helvetica", 12))
submit_button.pack(side=LEFT, padx=5)
# Chnage the cursour to start in the url_entry field
url_entry.focus_set()

# Define the function that clears the url_entry field
def clear_entry():
    url_entry.delete(0, END)

# Create the button that clears the field
cancel_button = Button(button_frame, text="Clear", command=clear_entry, bg="red", fg="white", font=("Helvetica", 12))
cancel_button.pack(side=LEFT, padx=5)

# Create a StringVar to store the selected option
selected_option = StringVar(gui)
# Create a list of options for the drop-down menu
options = ["Please select an option:","mp3","mp4"]
# Set the default value of the selected_option variable
selected_option.set(options[0])
# Create the drop-down menu
menu = OptionMenu(gui, selected_option, *options)
menu.pack(expand=True, pady=10)
# Change the dimensions of the menu
menu.config(width=20, height=1, bg="#303536", fg="white", font=("Helvetica", 12))

def download():
    if yt is None:
        messagebox.showerror("Error", "Please enter a valid URL and click Submit before downloading.")
        return

    option = selected_option.get()
    if option == "mp4":
        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()
        # Download the video
        stream.download()
        messagebox.showinfo("Download started", "The download has started and may take some time depending on your internet connection. The downloaded file can be found in the same folder as this script.")
    elif option == "mp3":
        # Get the audio only stream
        stream = yt.streams.filter(only_audio=True).first()
        # Download the audio
        stream.download()
        messagebox.showinfo("Download started", "The download has started and may take some time depending on your internet connection. The downloaded file can be found in the same folder as this script.")
    else:
        messagebox.showerror("Error", "Please select a valid option from the drop-down menu before downloading.")

download_button = Button(gui, text="Download", command=download, bg="blue", fg="white", font=("Helvetica", 12))
download_button.pack(pady=10)

# Credits message
def msgCallBack():
    messagebox.showinfo("Credits", "Made my myself, r3dwh33lb4rrow, and MysteriousMoff")

btn = tkinter.Button(gui, text ="Credits", command=msgCallBack, fg="white", bg="#303536")
btn.pack(side=BOTTOM)

# Start the infinite window loop
gui.mainloop()