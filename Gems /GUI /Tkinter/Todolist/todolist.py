import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("ToDo App")
        self.master.geometry("400x400")
        self.master.configure(bg="light green")

        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        # Task Entry
        tk.Label(self.master, text="Enter Your Task", bg="light green").grid(row=0, column=0, columnspan=2, pady=5)
        self.task_entry = tk.Entry(self.master, width=40)
        self.task_entry.grid(row=1, column=0, columnspan=2, pady=5)

        # Buttons
        tk.Button(self.master, text="Add Task", command=self.add_task, bg="light blue").grid(row=2, column=0, pady=5, padx=5)
        tk.Button(self.master, text="Update Task", command=self.update_task, bg="light blue").grid(row=2, column=1, pady=5, padx=5)

        # Task List
        self.task_listbox = tk.Listbox(self.master, width=50, height=10)
        self.task_listbox.grid(row=3, column=0, columnspan=2, pady=5, padx=5)
        self.task_listbox.bind('<<ListboxSelect>>', self.on_task_select)

        # Delete and Exit Buttons
        tk.Button(self.master, text="Delete Task", command=self.delete_task, bg="light blue").grid(row=4, column=0, pady=5, padx=5)
        tk.Button(self.master, text="Exit", command=self.master.quit, bg="light blue").grid(row=4, column=1, pady=5, padx=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def update_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            updated_task = self.task_entry.get().strip()
            if updated_task:
                self.tasks[index] = updated_task
                self.update_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter an updated task.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks, 1):
            self.task_listbox.insert(tk.END, f"[{i}] {task}")

    def on_task_select(self, event):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            task = self.tasks[index]
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
