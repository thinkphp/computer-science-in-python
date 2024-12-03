from tkinter import *
import tkinter.messagebox as tkmsg
from PIL import ImageTk, Image
import pyshorteners
import clipboard
import re

# Function to validate URL
def is_valid_url(url):
    if not url:
        return False

    regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, url) is not None

# Function to shorten URL
def convert():
    url_text = url.get().strip()  # Get and strip any leading/trailing whitespace

    if not is_valid_url(url_text):
        tkmsg.showerror("Invalid URL", "Please enter a valid URL.")
        return

    try:
        s = pyshorteners.Shortener().tinyurl.short(url_text)
        shorturl.set(s)

        # Clear and set clipboard
        root.clipboard_clear()
        root.clipboard_append(s)
        root.update()  # Now it stays on the clipboard after the window is closed

        Label(root, text="Shortened URL is copied to clipboard; press shift + Insert to paste", bg="#49f6b3", fg="#1e1e1e", font="poppins 9").place(x=8, y=360)
    except Exception as e:
        tkmsg.showerror("Error", f"An error occurred: {e}")

# Initializing the tkinter root window
root = Tk()
root.title("URL Shortener")
root.geometry("400x400")
root.resizable(False, False)

root.config(background="#4a536b")

# Loading and setting the background image
image = Image.open('bg3.png')
test = ImageTk.PhotoImage(image)
label = Label(root, image=test, bg="#4a536b")
label.pack()

url = StringVar()
shorturl = StringVar()

# UI Components
Label(root, text="Enter URL Here", bg="#2C3E50", fg="#EAECEE", font="poppins 13 bold", padx=3, pady=1).place(x=7, y=130)
Entry(root, textvariable=url, width=35, font="poppins 12").place(x=7, y=155)

Label(root, text="Shortened URL", bg="#2C3E50", fg="#fff", font="poppins 13 bold", padx=3, pady=1).place(x=8, y=300)
short = Entry(root, textvariable=shorturl, width=35, font="poppins 12")
short.place(x=8, y=325)

Button(root, text="Shorten URL", bg="#F8C471", fg="#1e1e1e", font="poppins 11 bold", command=convert, relief=GROOVE).place(x=8, y=220)

root.mainloop()
