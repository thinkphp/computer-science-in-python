import tkinter as tk
from tkinter import messagebox
import requests

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
API_KEY = ''
           
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    try:
        # Make a request to the OpenWeatherMap API
        response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
        data = response.json()
        print(data)
        if response.status_code == 200:
            # Extract weather information
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            return f"Weather: {weather}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
        else:
            return "City not found or API request error."
    except requests.RequestException as e:
        return f"Error: {e}"

def display_weather():
    city = entry_city.get()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name.")
        return

    weather_info = get_weather(city)
    text_result.config(state=tk.NORMAL)
    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, weather_info)
    text_result.config(state=tk.DISABLED)

# Create the main application window
root = tk.Tk()
root.title("Weather App")

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=20)

# Label and entry for the city name
label_city = tk.Label(input_frame, text="Enter city name:", font=("Arial", 14))
label_city.pack(side=tk.LEFT, padx=10)

entry_city = tk.Entry(input_frame, width=20, font=("Arial", 14))
entry_city.pack(side=tk.LEFT)

# Button to fetch weather
button_get_weather = tk.Button(input_frame, text="Get Weather", command=display_weather, font=("Arial", 14))
button_get_weather.pack(side=tk.LEFT, padx=10)

# Text widget to display the weather information
text_result = tk.Text(root, height=6, width=50, font=("Arial", 14), wrap=tk.WORD, state=tk.DISABLED)
text_result.pack(pady=20)

# Run the main event loop
root.mainloop()
