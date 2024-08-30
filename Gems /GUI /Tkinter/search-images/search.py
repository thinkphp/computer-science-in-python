import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

API_KEY = "EKSSKEBJ7phFLCyY6taO8p2ztknCH0MT6rO3I1CenslqMdEL9nLT19pM"
API_URL = "https://api.pexels.com/v1/search"

class ImageSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Search from API")

        # Search box
        self.search_var = tk.StringVar()
        self.search_box = tk.Entry(self.root, textvariable=self.search_var, width=50)
        self.search_box.pack(side="top", padx=10, pady=10)

        # Search button
        self.search_button = tk.Button(self.root, text="Search", command=self.search_images)
        self.search_button.pack(side="top", pady=5)

        # Image container
        self.image_container = tk.Frame(self.root)
        self.image_container.pack(fill="both", expand=True)

        # Scrollbar
        self.canvas = tk.Canvas(self.image_container)
        self.scroll_y = ttk.Scrollbar(self.image_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scroll_y.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scroll_y.pack(side="right", fill="y")

    def search_images(self):
        query = self.search_var.get()
        headers = {
            "Authorization": API_KEY
        }
        params = {
            "query": query,
            "per_page": 10,  # Number of results per page
            "page": 1  # Which page of results to retrieve
        }

        response = requests.get(API_URL, headers=headers, params=params)
        if response.status_code == 200:
            self.display_images(response.json())
        else:
            print("Error:", response.status_code)

    def display_images(self, data):
        # Clear the current images
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        photos = data['photos']
        for idx, photo in enumerate(photos):
            img_url = photo['src']['medium']
            response = requests.get(img_url)
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img.thumbnail((150, 150))
            img = ImageTk.PhotoImage(img)

            img_label = tk.Label(self.scrollable_frame, image=img)
            img_label.grid(row=idx // 5, column=idx % 5, padx=5, pady=5)
            img_label.image = img

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSearchApp(root)
    root.mainloop()

