import tkinter as tk
from tkinter import messagebox
import hashlib

def hash_password( password ):

    return hashlib.sha256( password.encode() ).hexdigest()

class User:

    def __init__(self, username, password, balance=0):

        #username pentru utilizator
        self.username = username
        #parola pentru utilizator
        self.password = hash_password( password )

        #balance
        self.balance = balance
        #se creeaza o lista in care stocam tranzactiile
        self.transactions = []

    def check_password(self, password):
        return self.password == hash_password(password)

    def add_transactions(self, transaction):
        self.transactions.append( transaction )

class BankSystem:

    def __init__(self):

        #aici stocam toti users bancii
        self.users = {}

    def create_user(self, username, password):
        if username in self.users:
           return False
        self.users[ username ] = User(username, password)
        return True

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if user and user.check_password(password):
            return user
        return None

class BankApplication:

    def __init__(self, root, bank_system):

        self.root = root
        self.root.title("Banking System")
        self.bank_system = bank_system
        self.current_user = None
        self.login_screen()

    def login_screen(self):
        self.clear_screen()
        font_label = ("Helvetica", 50)
        tk.Label(self.root, text = "Username:", font = font_label).pack()
        self.username_entry = tk.Entry(self.root, font = font_label)
        self.username_entry.pack()

        tk.Label(self.root, text = "Password:", font = font_label).pack()
        self.password_entry = tk.Entry(self.root, show = "*", font = font_label)
        self.password_entry.pack()

        tk.Button(self.root, text = "Login", command = self.login_account , font = font_label).pack()
        tk.Button(self.root, text = "Create Account", command = self.create_account, font = font_label).pack()

    def main_menu(self):
        self.clear_screen()
        font_label = ("Helvetica", 30)
        tk.Label(self.root, text = f"Welcome, {self.current_user.username}", font = font_label, fg = "green").pack(padx=10, pady=10)
        tk.Button(self.root, text = "Check Balance", command = self.check_balance, font = font_label).pack(padx=10, pady=10)
        tk.Button(self.root, text = "View Transactions", command = self.view_transactions, font = font_label).pack(padx=10, pady=10)
        tk.Button(self.root, text = "Transfer Money", command = self.transfer_money_screen, font = font_label).pack(padx=10, pady=10)
        tk.Button(self.root, text = "Top Up", font = font_label, command = self.top_up_screen).pack(padx=10, pady=10)#adaugam money, deposit
        tk.Button(self.root, text = "Logout", font = font_label, command = self.logout).pack(padx=10, pady=10)

    def check_balance( self ):
        messagebox.showinfo("Balance:",f"Your balance is: ${self.current_user.balance}")

    def logout(self):

        self.current_user = None
        self.login_screen()

    def clear_screen(self):
        for a in self.root.winfo_children():
            a.destroy()

    def login_account(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        user = self.bank_system.authenticate_user(username, password)

        if user:
           self.current_user = user
           self.main_menu()
        else:
           messagebox.showerror("Error","Invalid username or Password")
           self.login_screen()

    def create_account(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.bank_system.create_user( username, password ):

            messagebox.showinfo("Success", "Account created successfully!")
            self.login_screen()
        else:
            messagebox.showerror("Error","Username already exists!")
            self.login_screen()

    def top_up_screen(self):

        font_label = ("Helvetica", 50)
        self.clear_screen()
        tk.Label(self.root, text="Top-up amount", font = font_label).pack()
        amount_entry = tk.Entry(self.root, font = font_label)
        amount_entry.pack()

        tk.Button(self.root, text = "Top Up", font = font_label, command = lambda: self.top_up(amount_entry.get())).pack()
        tk.Button(self.root, text = "Back", font = font_label, command = self.main_menu).pack()

    def top_up(self, amount):

        if not amount.isdigit():
            messagebox.showerror("Error","Please enter a valid amount for balance!")
            return
        amount = int(amount)

        if amount <= 0:
            messagebox.showerror("Error","Amount must be positive.")
            return

        self.current_user.balance += amount
        self.current_user.add_transactions(f"Top-Up ${amount}")

        messagebox.showinfo("Success","Top-Up completed successfully!")
        self.main_menu()

    def view_transactions(self):
        font_label = ("Helvetica", 50)
        self.clear_screen()
        tk.Label(self.root, text = "Transactions History", font = font_label, fg = "green").pack()
        for transaction in self.current_user.transactions:
             tk.Label(self.root, text = transaction, font = font_label).pack()
        tk.Button(self.root, text = "Back", command = self.main_menu, font = font_label).pack()

    def transfer_money_screen(self):

        font_label = ("Helvetica", 50)
        self.clear_screen()

        #recipient
        tk.Label(self.root, text = "Recipient Username:", font = font_label).pack()
        recipient_entry = tk.Entry(self.root, font = font_label)
        recipient_entry.pack()

        #amount
        tk.Label(self.root, text = "Amount:", font = font_label).pack()
        amount_entry = tk.Entry(self.root, font = font_label)
        amount_entry.pack()

        #transfer
        tk.Button(self.root, text = "Transfer", font = font_label, command = lambda: self.transfer_money(recipient_entry.get(), amount_entry.get())).pack()

        #return to main menu
        tk.Button(self.root, text = "Back", command = self.main_menu, font = font_label).pack()

    def transfer_money(self, recipient_username, amount):
        #print(recipient_username)
        #print(amount)

        if not amount.isdigit():
            messagebox.showerror("Error","Please enter a valid amount of money!")
            return
        #convertim la intreg
        amount = int(amount)

        if amount <= 0:
            messagebox.showerror("Error","Amount must be positive!")
            return

        recipient = self.bank_system.users.get( recipient_username )

        if recipient and recipient != self.current_user:

            if self.current_user.balance >= amount:
                self.current_user.balance -= amount
                recipient.balance += amount

                self.current_user.add_transactions(f"Trasferred ${amount} to {recipient_username}")
                recipient.add_transactions(f"Received #{amount} from {self.current_user.username}")

                messagebox.showinfo("Success","Transfer completed successfully!")
            else:
                messagebox.showerror("Error"," Insufficient funds.")

        else:
            messagebox.showerror("Error","Recipient not fouund or invalid!")
        self.main_menu()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x500")
    bank_system = BankSystem()
    app = BankApplication(root, bank_system)
    root.mainloop()
