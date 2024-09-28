# Tkinter GUI App Desktop

Tkinter is Python's standard GUI (Graphical User Interface) package. It provides a fast and easy way to create GUI applications. Let's look at three examples to get started.

## Course Outline

1. Introduction to Tkinter
   - What is Tkinter?
   - Setting up the development environment
   - Creating your first Tkinter application

2. Tkinter Widgets
   - Basic widgets (Label, Button, Entry)
   - Advanced widgets (Listbox, Checkbutton, Radiobutton)
   - Container widgets (Frame, LabelFrame)

3. Layout Management
   - Pack geometry manager
   - Grid geometry manager
   - Place geometry manager

4. Event Handling
   - Button clicks
   - Keyboard events
   - Mouse events

5. Menus and Dialogs
   - Creating menus
   - Message boxes
   - File dialogs

6. Styling and Themes
   - Configuring widget appearance
   - Using ttk themed widgets
   - Creating custom styles

7. Advanced Topics
   - Canvas widget for drawing
   - Working with images
   - Creating scrollable widgets

8. Best Practices and Project
   - Code organization
   - Error handling
   - Final project: Building a complete application



Example 1: Hello, World! 
This example creates a window with a "Hello, World!" label.

```
import tkinter as tk

root = tk.Tk()
root.title("Hello, World!")

label = tk.Label(root, text="Hello, World!")
label.pack(padx=20, pady=20)

root.mainloop()
```

Example 2: Button Click
This example demonstrates how to create a button and handle a click event.

```
import tkinter as tk

def button_click():
    print("Button clicked!")

root = tk.Tk()
root.title("Button Example")

button = tk.Button(root, text="Click me!", command=button_click)
button.pack(padx=20, pady=20)

root.mainloop()
```

Example 3: Entry Widget
This example shows how to use an Entry widget to get user input.
```
import tkinter as tk

def submit():
    name = entry.get()
    print(f"Hello, {name}!")

root = tk.Tk()
root.title("Entry Widget Example")

label = tk.Label(root, text="Enter your name:")
label.pack(padx=10, pady=5)

entry = tk.Entry(root)
entry.pack(padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(padx=10, pady=10)

root.mainloop()
```

Advanced widgets. This example shows the usage of Listbox, Checkbutton, and Radiobutton widgets.
```
import tkinter as tk

root = tk.Tk()
root.title("Advanced Widgets")

# Listbox
listbox = tk.Listbox(root)
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.pack(pady=10)

# Checkbutton
var1 = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Choose me", variable=var1)
checkbutton.pack(pady=10)

# Radiobutton
var2 = tk.StringVar()
var2.set("option1")
radio1 = tk.Radiobutton(root, text="Option 1", variable=var2, value="option1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=var2, value="option2")
radio1.pack()
radio2.pack()

root.mainloop()
```
Container Widgets. This example demonstrates the use of Frame and LabelFrame container widgets.
```
import tkinter as tk

root = tk.Tk()
root.title("Container Widgets")

# Frame
frame = tk.Frame(root, borderwidth=2, relief="groove")
frame.pack(padx=10, pady=10)

label1 = tk.Label(frame, text="Inside Frame")
label1.pack(padx=5, pady=5)

button1 = tk.Button(frame, text="Frame Button")
button1.pack(padx=5, pady=5)

# LabelFrame
labelframe = tk.LabelFrame(root, text="LabelFrame", padx=5, pady=5)
labelframe.pack(padx=10, pady=10)

label2 = tk.Label(labelframe, text="Inside LabelFrame")
label2.pack()

button2 = tk.Button(labelframe, text="LabelFrame Button")
button2.pack()

root.mainloop()
```
