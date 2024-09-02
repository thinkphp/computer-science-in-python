import tkinter as tk
import requests
from tkinter import messagebox

def shorten_url():
    long_url = entry.get()
    headers = {
        "Authorization": "Bearer your_bitly_access_token",
        "Content-Type": "application/json"
    }
    data = {"long_url": long_url}

    try:
        response = requests.post("https://api-ssl.bitly.com/v4/shorten", json=data, headers=headers)
        response.raise_for_status()
        shortened_url = response.json().get("link")
        label.config(text=f"Shortened URL: {shortened_url}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to shorten URL: {e}")

# Create the main window
root = tk.Tk()  
root.title("URL Shortener")

# Set the minimum size of the window
root.geometry("500x200")
root.minsize(500, 200)

# Increase the font size for clarity
font_large = ("Arial", 14)
font_small = ("Arial", 12)

# Create an Entry widget for the long URL with a larger font
entry = tk.Entry(root, width=50, font=font_large)
entry.pack(padx=10, pady=20)

# Create a Button to trigger the URL shortening with a larger font
button = tk.Button(root, text="Shorten", command=shorten_url, font=font_large)
button.pack(pady=10)

# Create a Label to display the shortened URL with a larger font
label = tk.Label(root, text="", font=font_small)
label.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
