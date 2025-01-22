import tkinter as tk
from tkinter import ttk

def check_palindrome():
    # Get text from entry and clean it
    text = entry.get().lower()
    # Remove spaces and punctuation
    cleaned_text = ''.join(char for char in text if char.isalnum())

    if not cleaned_text:
        result_label.configure(text="Please enter some text")
        result_label.configure(style='Black.TLabel')
        return

    # Check if it's a palindrome
    is_palindrome = cleaned_text == cleaned_text[::-1]

    # Update result with appropriate color and message
    if is_palindrome:
        result_label.configure(
            text=f'"{text}" is a palindrome!',
            style='Green.TLabel'
        )
    else:
        result_label.configure(
            text=f'"{text}" is not a palindrome',
            style='Red.TLabel'
        )

# Create main window
root = tk.Tk()
root.title("Palindrome Checker")
root.geometry("400x200")

# Create styles for colored labels
style = ttk.Style()
style.configure('Green.TLabel', foreground='green')
style.configure('Red.TLabel', foreground='red')
style.configure('Black.TLabel', foreground='black')

# Create and configure frame
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create and place widgets
title_label = ttk.Label(
    frame,
    text="Enter text to check if it's a palindrome:",
    font=('Helvetica', 12)
)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

entry = ttk.Entry(frame, width=40)
entry.grid(row=1, column=0, columnspan=2, pady=10)

check_button = ttk.Button(
    frame,
    text="Check Palindrome",
    command=check_palindrome
)
check_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = ttk.Label(
    frame,
    text="Result will appear here",
    font=('Helvetica', 10),
    style='Black.TLabel'
)
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Configure grid weights
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# Bind Enter key to check_palindrome function
root.bind('<Return>', lambda e: check_palindrome())

# Start the main event loop
root.mainloop()
