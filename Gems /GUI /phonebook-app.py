import tkinter as tk
from tkinter import messagebox, simpledialog
import re

# Validare email
def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Validare nume (doar litere și spații)
def validate_name(name):
    return bool(re.match(r"^[A-Za-z\s]+$", name))

# Validare număr de telefon (doar cifre și caractere speciale permit)
def validate_phone(phone):
    return bool(re.match(r"^[\d+\-\(\)\s]+$", phone))

# Funcție pentru adăugarea unui nou contact în dicționarul de contacte
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    if not name or not phone:
        messagebox.showerror("Error", "Name and phone number are required!")
        return

    if not validate_name(name):
        messagebox.showerror("Error", "Invalid name format! Only letters and spaces are allowed.")
        return

    if not validate_phone(phone):
        messagebox.showerror("Error", "Invalid phone number format! Only digits and certain special characters are allowed.")
        return

    if email and not validate_email(email):
        messagebox.showerror("Error", "Invalid email format!")
        return

    if name and phone:
        contacts[name] = {'Phone': phone, 'Email': email}
        update_contact_list()
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
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
    details = contacts.get(selected_contact, {})
    details_text.config(text=f"Phone: {details.get('Phone', '')}\nEmail: {details.get('Email', '')}")

# Funcție pentru ștergerea unui contact selectat din dicționar și interfața grafică
def delete_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete contact '{selected_contact}'?"):
            del contacts[selected_contact]
            update_contact_list()
            details_text.config(text="")
            messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showerror("Error", "No contact selected!")

# Funcție pentru editarea unui contact selectat
def edit_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        new_name = simpledialog.askstring("Edit Contact", "Enter new name:", initialvalue=selected_contact)
        if new_name:
        
            if new_name in contacts:
                messagebox.showerror("Error", "Contact with this name already exists!")
                return
            if not validate_name(new_name):
                messagebox.showerror("Error", "Invalid name format! Only letters and spaces are allowed.")
                return
                
            new_phone = simpledialog.askstring("Edit Contact", "Enter new phone:", initialvalue=contacts[selected_contact]['Phone'])
            new_email = simpledialog.askstring("Edit Contact", "Enter new email:", initialvalue=contacts[selected_contact]['Email'])
            if new_phone:
                if not validate_phone(new_phone):
                    messagebox.showerror("Error", "Invalid phone number format! Only digits and certain special characters are allowed.")
                    return
                
                if new_email and not validate_email(new_email):
                    messagebox.showerror("Error", "Invalid email format!")
                    return
                contacts.pop(selected_contact)
                contacts[new_name] = {'Phone': new_phone, 'Email': new_email}
                update_contact_list()
                details_text.config(text="")
                messagebox.showinfo("Success", "Contact edited successfully!")
            else:
                messagebox.showerror("Error", "Phone number is required!")
    else:
        messagebox.showerror("Error", "No contact selected!")

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

# Butoane pentru editarea și ștergerea unui contact selectat
edit_button = tk.Button(root, text="Edit Contact", command=edit_contact)
edit_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack(pady=5)

root.mainloop()
