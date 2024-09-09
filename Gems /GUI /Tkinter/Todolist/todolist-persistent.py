import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import pickle
import os

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __str__(self):
        return f"{'[X]' if self.completed else '[ ]'} {self.description}"

class ToDoListGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.master.geometry("400x300")

        self.tasks = []
        self.save_file = "tasks.pkl"

        # Task list
        self.task_listbox = tk.Listbox(self.master, width=50)
        self.task_listbox.pack(pady=10)

        # Input field
        self.task_entry = tk.Entry(self.master, width=40)
        self.task_entry.pack()

        # Buttons
        button_frame = ttk.Frame(self.master)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Add Task", command=self.add_task).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Mark Completed", command=self.mark_completed).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Update Task", command=self.update_task).grid(row=0, column=2, padx=5)
        ttk.Button(button_frame, text="Delete Task", command=self.delete_task).grid(row=0, column=3, padx=5)

        self.load_tasks()
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        description = self.task_entry.get().strip()
        if description:
            task = Task(description)
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, str(task))
            self.task_entry.delete(0, tk.END)
            self.save_tasks()

    def mark_completed(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index].completed = True
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, str(self.tasks[index]))
            self.save_tasks()

    def update_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            new_description = simpledialog.askstring("Update Task", "Enter new task description:",
                                                     initialvalue=self.tasks[index].description)
            if new_description:
                self.tasks[index].description = new_description
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, str(self.tasks[index]))
                self.save_tasks()

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.task_listbox.delete(index)
            self.save_tasks()

    def load_tasks(self):
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, 'rb') as f:
                    self.tasks = pickle.load(f)
                for task in self.tasks:
                    self.task_listbox.insert(tk.END, str(task))
                print(f"Tasks loaded successfully. Total tasks: {len(self.tasks)}")
            except Exception as e:
                messagebox.showerror("Error", f"Error loading tasks: {str(e)}")
        else:
            print("Save file does not exist. Starting with empty task list.")

    def save_tasks(self):
        try:
            with open(self.save_file, 'wb') as f:
                pickle.dump(self.tasks, f)
            print(f"Tasks saved successfully. Total tasks: {len(self.tasks)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving tasks: {str(e)}")

    def on_closing(self):
        self.save_tasks()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListGUI(root)
    root.mainloop()
