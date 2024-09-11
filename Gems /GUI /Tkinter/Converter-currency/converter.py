import tkinter as tk
from tkinter import ttk
import requests
import os

def get_exchange_rates(api_key):
    """Retrieves exchange rates from a free API using the provided API key."""
    try:
        response = requests.get(f"https://openexchangerates.org/api/latest.json?app_id={api_key}")
        data = response.json()

        # Handle expected API structure
        if "rates" in data:
            return data["rates"]
        else:
            print("API response structure may have changed. Update the code to access the correct key.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None

def convert_currency():
    """Converts the specified amount from the source currency to the target currency."""
    try:
        amount = float(amount_entry.get())
        source_currency = source_currency_combo.get()
        target_currency = target_currency_combo.get()

        api_key = os.environ.get("EXCHANGE_API_KEY")
        print(api_key)
        if not api_key:
            print("API key not found. Please set the EXCHANGE_API_KEY environment variable.")
            return

        exchange_rates = get_exchange_rates(api_key)
        if exchange_rates:
            source_rate = exchange_rates[source_currency]
            target_rate = exchange_rates[target_currency]
            converted_amount = amount * target_rate / source_rate
            result_label.config(text=f"{amount} {source_currency} = {converted_amount:.2f} {target_currency}")
        else:
            result_label.config(text="Error fetching exchange rates. Please try again.")
    except ValueError:
        result_label.config(text="Invalid amount. Please enter a valid number.")

# Create the main window
window = tk.Tk()
window.title("Currency Converter")
window.geometry("700x200")

# Define a larger font
large_font = ("Arial", 24)

# Create labels and entry fields with larger fonts
amount_label = ttk.Label(window, text="Amount:", font=large_font)
amount_entry = ttk.Entry(window, font=large_font)
source_currency_label = ttk.Label(window, text="Source Currency:", font=large_font)
source_currency_combo = ttk.Combobox(window, state="readonly", font=large_font)
target_currency_label = ttk.Label(window, text="Target Currency:", font=large_font)
target_currency_combo = ttk.Combobox(window, state="readonly", font=large_font)
convert_button = ttk.Button(window, text="Convert", command=convert_currency, style="TButton")
result_label = ttk.Label(window, text="", font=large_font)

# Arrange widgets
amount_label.grid(row=0, column=0)
amount_entry.grid(row=0, column=1)
source_currency_label.grid(row=1, column=0)
source_currency_combo.grid(row=1, column=1)
target_currency_label.grid(row=2, column=0)
target_currency_combo.grid(row=2, column=1)
convert_button.grid(row=3, column=0, columnspan=2)
result_label.grid(row=4, column=0, columnspan=2)

# Populate currency comboboxes
#api_key = "292a5c4329cf4b8fa3462d4c851417d0"
api_key = os.environ.get("EXCHANGE_API_KEY")
if not api_key:
    print("API key not found. Please set the EXCHANGE_API_KEY environment variable.")
    exit()

exchange_rates = get_exchange_rates( api_key )
if exchange_rates:
    currencies = list(exchange_rates.keys())
    source_currency_combo["values"] = currencies
    target_currency_combo["values"] = currencies
else:
    result_label.config(text="Error fetching exchange rates. Please try again.")

# Start the main loop
window.mainloop()
