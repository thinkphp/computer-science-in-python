import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO
import threading

class BookSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Google Books Search")
        self.root.geometry("800x600")

        # Query, max results, and start index variables
        self.query_var = tk.StringVar()
        self.max_results_var = tk.IntVar(value=12)
        self.start_index_var = tk.IntVar(value=1)

        # Loading indicator variable
        self.loading_var = tk.StringVar(value="")

        # Creating the search UI
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        # Search entry
        tk.Label(frame, text="Search Books:").grid(row=0, column=0, padx=5, pady=5)
        search_entry = tk.Entry(frame, textvariable=self.query_var, width=50)
        search_entry.grid(row=0, column=1, padx=5, pady=5)
        search_entry.bind("<Return>", self.handle_search)

        # Max results
        tk.Label(frame, text="Max Results:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(frame, textvariable=self.max_results_var, width=10).grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Start index
        tk.Label(frame, text="Start Index:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(frame, textvariable=self.start_index_var, width=10).grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Search button
        search_button = tk.Button(frame, text="Search", command=self.handle_search)
        search_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Loading indicator
        self.loading_label = tk.Label(self.root, textvariable=self.loading_var, font=("Arial", 12))
        self.loading_label.pack(pady=10)

        # Scrollable results frame
        self.canvas = tk.Canvas(self.root)
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def handle_search(self, event=None):
        query = self.query_var.get().strip()
        max_results = self.max_results_var.get()
        start_index = self.start_index_var.get()

        if not query:
            messagebox.showerror("Error", "Please enter a book title.")
            return

        if not (1 <= max_results <= 40):
            messagebox.showwarning("Warning", "Max results must be between 1 and 40.")
            return

        # Start loading indicator
        self.loading_var.set("Loading...")
        self.loading_label.update()

        # Use threading to prevent UI freeze during the search
        threading.Thread(target=self.search_books, args=(query, max_results, start_index)).start()

    def search_books(self, query, max_results, start_index):
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}&startIndex={start_index}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            items = data.get("items", [])
            if items:
                self.display_results(items)
            else:
                messagebox.showinfo("No Results", "No books found.")
        else:
            messagebox.showerror("Error", "Failed to fetch books data.")

        # Stop loading indicator
        self.loading_var.set("")

    def display_results(self, items):
        # Clear previous results
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for item in items:
            book_info = item["volumeInfo"]

            title = book_info.get("title", "N/A")
            authors = ", ".join(book_info.get("authors", ["Unknown"]))
            thumbnail_url = book_info.get("imageLinks", {}).get("thumbnail")

            # Frame for each book
            book_frame = tk.Frame(self.scrollable_frame, pady=10)
            book_frame.pack(fill="x")

            if thumbnail_url:
                response = requests.get(thumbnail_url)
                img_data = BytesIO(response.content)
                img = Image.open(img_data)
                img.thumbnail((100, 150))
                photo = ImageTk.PhotoImage(img)
                thumbnail_label = tk.Label(book_frame, image=photo)
                thumbnail_label.image = photo  # Keep a reference
                thumbnail_label.pack(side="left")

            # Book details
            details_frame = tk.Frame(book_frame)
            details_frame.pack(side="left", padx=10)

            tk.Label(details_frame, text=f"Title: {title}", font=("Arial", 14)).pack(anchor="w")
            tk.Label(details_frame, text=f"Authors: {authors}", font=("Arial", 12)).pack(anchor="w")

if __name__ == "__main__":
    root = tk.Tk()
    app = BookSearchApp(root)
    root.mainloop()
