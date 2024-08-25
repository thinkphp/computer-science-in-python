import tkinter as tk
from tkinter import messagebox
import json
import os
import bcrypt  # Import bcrypt for password hashing

# File to store user data
USER_DATA_FILE = 'user_data.json'

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._hash_password(password)

    def _hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def _check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def save(self):
        try:
            users = self.load_all_users()
            if self.username in users:
                raise ValueError("Username already exists")
            users[self.username] = self.password
            with open(USER_DATA_FILE, 'w') as file:
                json.dump(users, file)
        except IOError as e:
            messagebox.showerror("File Error", f"An error occurred while saving user data: {e}")

    @staticmethod
    def load_all_users():
        if os.path.exists(USER_DATA_FILE):
            with open(USER_DATA_FILE, 'r') as file:
                return json.load(file)
        return {}

    @staticmethod
    def authenticate(username, password):
        users = User.load_all_users()
        user_password = users.get(username)
        if user_password:
            return bcrypt.checkpw(password.encode('utf-8'), user_password.encode('utf-8'))
        return False

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Login System')
        self.current_frame = None
        self.current_user = None  # Store the current logged-in user
        self.show_login_screen()

    def show_login_screen(self):
        self._destroy_current_frame()
        self.current_frame = LoginScreen(self.root, self)

    def show_signup_screen(self):
        self._destroy_current_frame()
        self.current_frame = SignUpScreen(self.root, self)

    def show_menu_screen(self):
        self._destroy_current_frame()
        self.current_frame = MenuScreen(self.root, self, self.current_user)

    def set_current_user(self, username):
        self.current_user = username

    def _destroy_current_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
            self.current_frame = None

class LoginScreen(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.app = app
        self.pack()

        self.username_label = tk.Label(self, text='Username')
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text='Password')
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack()

        self.login_button = tk.Button(self, text='Login', command=self.login)
        self.login_button.pack()

        self.signup_button = tk.Button(self, text='Sign Up', command=self.app.show_signup_screen)
        self.signup_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if User.authenticate(username, password):
            self.app.set_current_user(username)  # Set the current user
            self.app.show_menu_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def destroy(self):
        super().destroy()

class SignUpScreen(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.app = app
        self.pack()

        self.username_label = tk.Label(self, text='Username')
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text='Password')
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack()

        self.signup_button = tk.Button(self, text='Sign Up', command=self.signup)
        self.signup_button.pack()

        self.login_button = tk.Button(self, text='Back to Login', command=self.app.show_login_screen)
        self.login_button.pack()

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            try:
                user = User(username, password)
                user.save()
                messagebox.showinfo("Sign Up Successful", "User registered successfully")
                self.app.show_login_screen()
            except ValueError:
                messagebox.showerror("Sign Up Failed", "Username already exists")
        else:
            messagebox.showerror("Input Error", "Username and password cannot be empty")

    def destroy(self):
        super().destroy()

class MenuScreen(tk.Frame):
    def __init__(self, root, app, username):
        super().__init__(root)
        self.app = app
        self.username = username  # Store the username
        self.pack()

        self.label = tk.Label(self, text=f'Welcome, {self.username}!')
        self.label.pack()

        self.logout_button = tk.Button(self, text='Logout', command=self.logout)
        self.logout_button.pack()

    def logout(self):
        self.app.set_current_user(None)  # Clear the current user
        self.app.show_login_screen()

    def destroy(self):
        super().destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
