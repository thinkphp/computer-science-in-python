import tkinter as tk
from tkinter import messagebox
import hashlib
import json
import os

# Utility function for password hashing
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

class User:
    def __init__(self, username, password, balance=0, transactions=None, is_hashed=False):
        self.username = username
        if is_hashed:
            self.password = password  # Use the pre-hashed password
        else:
            self.password = hash_password(password)  # Hash the plaintext password
        self.balance = balance
        self.transactions = transactions if transactions is not None else []

    def check_password(self, password):
        return self.password == hash_password(password)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

class BankSystem:
    def __init__(self, data_file="bank_data.json"):
        self.data_file = data_file
        self.users = self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                users = {}
                for username, info in data.items():
                    users[username] = User(
                        username,
                        password=info['password'],  # Pre-hashed password
                        balance=info['balance'],
                        transactions=info['transactions'],
                        is_hashed=True  # Indicate that the password is already hashed
                    )
                return users
        return {}

    def save_data(self):
        data = {username: {
                    "password": user.password,
                    "balance": user.balance,
                    "transactions": user.transactions
                } for username, user in self.users.items()}
        with open(self.data_file, 'w') as file:
            json.dump(data, file, indent=4)

    def create_user(self, username, password):
        if username in self.users:
            return False
        self.users[username] = User(username, password)
        self.save_data()
        return True

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if user and user.check_password(password):
            return user
        return None

class BankApp:
    def __init__(self, root, bank_system):
        self.root = root
        self.root.title("Banking System")
        self.bank_system = bank_system
        self.current_user = None
        self.font = ("Arial", 14)  # Define the font and size
        self.login_screen()

    def login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Username", font=self.font).pack()
        username_entry = tk.Entry(self.root, font=self.font)
        username_entry.pack()

        tk.Label(self.root, text="Password", font=self.font).pack()
        password_entry = tk.Entry(self.root, show="*", font=self.font)
        password_entry.pack()

        tk.Button(self.root, text="Login", font=self.font, command=lambda: self.login(username_entry.get(), password_entry.get())).pack()
        tk.Button(self.root, text="Create Account", font=self.font, command=lambda: self.create_account(username_entry.get(), password_entry.get())).pack()

    def create_account(self, username, password):
        if self.bank_system.create_user(username, password):
            messagebox.showinfo("Success", "Account created successfully!")
        else:
            messagebox.showerror("Error", "Username already exists.")
        self.login_screen()

    def login(self, username, password):
        user = self.bank_system.authenticate_user(username, password)
        if user:
            self.current_user = user
            self.main_menu()
        else:
            messagebox.showerror("Error", "Invalid username or password.")
            self.login_screen()

    def main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text=f"Welcome, {self.current_user.username}", font=self.font).pack()
        tk.Button(self.root, text="Check Balance", font=self.font, command=self.check_balance).pack()
        tk.Button(self.root, text="View Transactions", font=self.font, command=self.view_transactions).pack()
        tk.Button(self.root, text="Add Money", font=self.font, command=self.add_money_screen).pack()
        tk.Button(self.root, text="Transfer Money", font=self.font, command=self.transfer_money_screen).pack()
        tk.Button(self.root, text="Logout", font=self.font, command=self.logout).pack()

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your balance is: ${self.current_user.balance}")

    def view_transactions(self):
        self.clear_screen()
        tk.Label(self.root, text="Transaction History", font=self.font).pack()
        for transaction in self.current_user.transactions:
            tk.Label(self.root, text=transaction, font=self.font).pack()
        tk.Button(self.root, text="Back", font=self.font, command=self.main_menu).pack()

    def add_money_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Enter amount to add:", font=self.font).pack()
        amount_entry = tk.Entry(self.root, font=self.font)
        amount_entry.pack()

        tk.Button(self.root, text="Add Money", font=self.font, command=lambda: self.add_money(amount_entry.get())).pack()
        tk.Button(self.root, text="Back", font=self.font, command=self.main_menu).pack()

    def add_money(self, amount):
        if not amount.isdigit():
            messagebox.showerror("Error", "Please enter a valid amount.")
            return

        amount = int(amount)
        self.current_user.balance += amount
        self.current_user.add_transaction(f"Added ${amount} to balance")

        self.bank_system.save_data()

        messagebox.showinfo("Success", f"${amount} added to your account.")
        self.main_menu()

    def transfer_money_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Recipient Username", font=self.font).pack()
        recipient_entry = tk.Entry(self.root, font=self.font)
        recipient_entry.pack()

        tk.Label(self.root, text="Amount", font=self.font).pack()
        amount_entry = tk.Entry(self.root, font=self.font)
        amount_entry.pack()

        tk.Button(self.root, text="Transfer", font=self.font, command=lambda: self.transfer_money(recipient_entry.get(), amount_entry.get())).pack()
        tk.Button(self.root, text="Back", font=self.font, command=self.main_menu).pack()

    def transfer_money(self, recipient_username, amount):
        if not amount.isdigit():
            messagebox.showerror("Error", "Please enter a valid amount.")
            return

        amount = int(amount)
        recipient = self.bank_system.users.get(recipient_username)

        if recipient and recipient != self.current_user:
            if self.current_user.balance >= amount:
                self.current_user.balance -= amount
                recipient.balance += amount

                self.current_user.add_transaction(f"Transferred ${amount} to {recipient_username}")
                recipient.add_transaction(f"Received ${amount} from {self.current_user.username}")

                self.bank_system.save_data()

                messagebox.showinfo("Success", "Transfer completed successfully!")
            else:
                messagebox.showerror("Error", "Insufficient funds.")
        else:
            messagebox.showerror("Error", "Recipient not found or invalid.")
        self.main_menu()

    def logout(self):
        self.current_user = None
        self.login_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    bank_system = BankSystem()
    app = BankApp(root, bank_system)
    root.mainloop()
