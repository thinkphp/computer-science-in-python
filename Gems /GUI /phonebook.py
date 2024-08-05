import tkinter as tk
from tkinter import messagebox

# Funcție pentru adăugarea unui nou contact în dicționarul de contacte
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()

    if name and phone:
        contacts[name] = {'Phone': phone, 'Email': email}
        update_contact_list()
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showerror("Error", "Name and phone number are required!")

# Funcție pentru actualizarea listei de contacte în interfața grafică
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name in contacts:
        contact_listbox.insert(tk.END, name)

# Funcție pentru afișarea detaliilor unui contact selectat în interfața grafică
def show_contact_details(event):
    selected_contact = contact_listbox.get(tk.ACTIVE)
    details = contacts[selected_contact]
    details_text.config(text=f"Phone: {details['Phone']}\nEmail: {details['Email']}")

# Dicționarul care va stoca contactele
contacts = {}

# Crearea și configurarea ferestrei principale
root = tk.Tk()
root.title("Contact Manager")

# Frame pentru adăugarea unui nou contact
frame_add_contact = tk.Frame(root)
frame_add_contact.pack(padx=10, pady=10)

tk.Label(frame_add_contact, text="Name:").grid(row=0, column=0, sticky='w')
entry_name = tk.Entry(frame_add_contact)
entry_name.grid(row=0, column=1, padx=5)

tk.Label(frame_add_contact, text="Phone:").grid(row=1, column=0, sticky='w')
entry_phone = tk.Entry(frame_add_contact)
entry_phone.grid(row=1, column=1, padx=5)

tk.Label(frame_add_contact, text="Email:").grid(row=2, column=0, sticky='w')
entry_email = tk.Entry(frame_add_contact)
entry_email.grid(row=2, column=1, padx=5)

add_button = tk.Button(frame_add_contact, text="Add Contact", command=add_contact)
add_button.grid(row=3, columnspan=2, pady=5)

# Frame pentru afișarea listei de contacte
frame_contact_list = tk.Frame(root)
frame_contact_list.pack(padx=10, pady=5)

tk.Label(frame_contact_list, text="Contacts:").pack()

contact_listbox = tk.Listbox(frame_contact_list, width=30, height=10)
contact_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame_contact_list, orient=tk.VERTICAL)
scrollbar.config(command=contact_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

contact_listbox.config(yscrollcommand=scrollbar.set)
contact_listbox.bind("<<ListboxSelect>>", show_contact_details)

# Frame pentru afișarea detaliilor unui contact selectat
frame_contact_details = tk.Frame(root)
frame_contact_details.pack(pady=5)

details_text = tk.Label(frame_contact_details, text="", justify=tk.LEFT)
details_text.pack()

root.mainloop()
