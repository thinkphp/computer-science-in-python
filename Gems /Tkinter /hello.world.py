import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Python App Title")
window.geometry("300x200")

label = tk.Label(window, text="Enter input value")
label.pack()

# Function to insert value at beginning in Entry field
def insert_value_in_entry():
    entry.insert(2, "Hello World ")

# Create an Entry field
entry = tk.Entry(window)
entry.pack()

# Create a button
button = tk.Button(window, text="Insert", command=insert_value_in_entry)
button.pack()

# Run the application
window.mainloop()
