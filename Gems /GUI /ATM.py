import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, account_number, pin, name, surname, birthday, user_id, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.user_id = user_id
        self.balance = balance

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def update_pin(self, new_pin):
        self.pin = new_pin

    def inquire_balance(self):
        return self.balance

    def withdraw_cash(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def deposit_cash(self, amount):
        self.balance += amount

class ATM:
    def __init__(self, master, users):
        self.master = master
        self.master.title("ATM Simulator")
        self.master.geometry("300x250")
        self.users = users
        self.current_user = None

        # Login screen
        self.login_screen()

    def login_screen(self):
        self.clear_window()

        self.lbl_account = tk.Label(self.master, text="Account Number:")
        self.lbl_account.pack()
        self.entry_account = tk.Entry(self.master)
        self.entry_account.pack()

        self.lbl_pin = tk.Label(self.master, text="PIN:")
        self.lbl_pin.pack()
        self.entry_pin = tk.Entry(self.master, show="*")
        self.entry_pin.pack()

        self.btn_login = tk.Button(self.master, text="Login", command=self.authenticate)
        self.btn_login.pack()

    def authenticate(self):
        account_number = self.entry_account.get()
        pin = self.entry_pin.get()

        for user in self.users:
            if user.account_number == account_number and user.check_pin(pin):
                self.current_user = user
                self.main_menu()
                return

        messagebox.showerror("Error", "Invalid account number or PIN")

    def main_menu(self):
        self.clear_window()

        # Display personalized welcome message
        welcome_message = f"Welcome back, {self.current_user.name}!"
        self.lbl_welcome = tk.Label(self.master, text=welcome_message)
        self.lbl_welcome.pack()

        self.btn_balance = tk.Button(self.master, text="Balance Inquiry", command=self.balance_inquiry)
        self.btn_balance.pack()

        self.btn_withdraw = tk.Button(self.master, text="Withdraw Cash", command=self.withdraw_cash)
        self.btn_withdraw.pack()

        self.btn_deposit = tk.Button(self.master, text="Deposit Cash", command=self.deposit_cash)
        self.btn_deposit.pack()

        self.btn_change_pin = tk.Button(self.master, text="Change PIN", command=self.change_pin)
        self.btn_change_pin.pack()

        self.btn_logout = tk.Button(self.master, text="Logout", command=self.login_screen)
        self.btn_logout.pack()

    def change_pin(self):
        self.clear_window()

        self.lbl_old_pin = tk.Label(self.master, text="Enter old PIN:")
        self.lbl_old_pin.pack()
        self.entry_old_pin = tk.Entry(self.master, show="*")
        self.entry_old_pin.pack()

        self.lbl_new_pin = tk.Label(self.master, text="Enter new PIN:")
        self.lbl_new_pin.pack()
        self.entry_new_pin = tk.Entry(self.master, show="*")
        self.entry_new_pin.pack()

        self.lbl_confirm_pin = tk.Label(self.master, text="Confirm new PIN:")
        self.lbl_confirm_pin.pack()
        self.entry_confirm_pin = tk.Entry(self.master, show="*")
        self.entry_confirm_pin.pack()

        self.btn_submit = tk.Button(self.master, text="Change PIN", command=self.perform_pin_change)
        self.btn_submit.pack()

        self.btn_back = tk.Button(self.master, text="Back", command=self.main_menu)
        self.btn_back.pack()

    def perform_pin_change(self):
        old_pin = self.entry_old_pin.get()
        new_pin = self.entry_new_pin.get()
        confirm_pin = self.entry_confirm_pin.get()

        if not self.current_user.check_pin(old_pin):
            messagebox.showerror("Error", "Old PIN is incorrect")
            return

        if new_pin != confirm_pin:
            messagebox.showerror("Error", "New PIN and confirmation do not match")
            return

        if len(new_pin) < 4:
            messagebox.showerror("Error", "New PIN must be at least 4 digits long")
            return

        self.current_user.update_pin(new_pin)
        messagebox.showinfo("Success", "PIN changed successfully")
        self.clear_window()
        self.main_menu()

    def balance_inquiry(self):
        balance = self.current_user.inquire_balance()
        messagebox.showinfo("Balance Inquiry", f"Your balance is: ${balance:.2f}")

    def withdraw_cash(self):
        self.clear_window()

        self.lbl_amount = tk.Label(self.master, text="Enter amount to withdraw:")
        self.lbl_amount.pack()
        self.entry_amount = tk.Entry(self.master)
        self.entry_amount.pack()

        self.btn_submit = tk.Button(self.master, text="Withdraw", command=self.perform_withdrawal)
        self.btn_submit.pack()

        self.btn_back = tk.Button(self.master, text="Back", command=self.main_menu)
        self.btn_back.pack()

    def perform_withdrawal(self):
        try:
            amount = float(self.entry_amount.get())
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            if self.current_user.withdraw_cash(amount):
                messagebox.showinfo("Success", f"Successfully withdrew ${amount:.2f}")
            else:
                messagebox.showerror("Error", "Insufficient balance")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid amount: {e}")
        self.clear_window()
        self.main_menu()

    def deposit_cash(self):
        self.clear_window()

        self.lbl_amount = tk.Label(self.master, text="Enter amount to deposit:")
        self.lbl_amount.pack()
        self.entry_amount = tk.Entry(self.master)
        self.entry_amount.pack()

        self.btn_submit = tk.Button(self.master, text="Deposit", command=self.perform_deposit)
        self.btn_submit.pack()

        self.btn_back = tk.Button(self.master, text="Back", command=self.main_menu)
        self.btn_back.pack()

    def perform_deposit(self):
        try:
            amount = float(self.entry_amount.get())
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            self.current_user.deposit_cash(amount)
            messagebox.showinfo("Success", f"Successfully deposited ${amount:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid amount: {e}")
        self.clear_window()
        self.main_menu()

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    # Create some users with additional information
    user1 = User("123456", "1111", "John", "Doe", "01/01/1990", "ID123456", 500)
    user2 = User("654321", "2222", "Jane", "Smith", "02/02/1985", "ID654321", 1000)
    user3 = User("111111", "3333", "Alice", "Johnson", "03/03/2000", "ID111111", 250)

    users = [user1, user2, user3]

    root = tk.Tk()
    atm = ATM(root, users)
    root.mainloop()
