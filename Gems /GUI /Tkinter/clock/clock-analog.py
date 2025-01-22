import tkinter as tk
import time
import math

class AnalogClock(tk.Canvas):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(background='white')
        self.create_clock_face()
        self.hands = {}
        self.create_hands()
        self.update_clock()

    def create_clock_face(self):
        # Create clock circle
        self.create_oval(10, 10, 290, 290, width=2)
        # Create hour numbers
        for i in range(12):
            angle = i * math.pi/6 - math.pi/2
            x = 150 + 140 * math.cos(angle)
            y = 150 + 140 * math.sin(angle)
            self.create_text(x, y, text=str(i+1), font=('Arial', 12, 'bold'))

    def create_hands(self):
        # Hour hand
        self.hands['hour'] = self.create_line(150, 150, 150, 80, width=6, fill='black')
        # Minute hand
        self.hands['minute'] = self.create_line(150, 150, 150, 60, width=4, fill='blue')
        # Second hand
        self.hands['second'] = self.create_line(150, 150, 150, 50, width=2, fill='red')
        # Center dot
        self.create_oval(145, 145, 155, 155, fill='black')

    def update_clock(self):
        # Get current time
        current_time = time.localtime()
        hours, minutes, seconds = current_time.tm_hour, current_time.tm_min, current_time.tm_sec

        # Calculate angles
        # Note: -90 degrees offset to start at 12 o'clock
        second_angle = math.radians(((seconds/60) * 360) - 90)
        minute_angle = math.radians(((minutes/60) * 360) - 90)
        hour_angle = math.radians(((hours/12 + minutes/720) * 360) - 90)

        # Update hand positions
        # Hour hand
        hour_x = 150 + 60 * math.cos(hour_angle)
        hour_y = 150 + 60 * math.sin(hour_angle)
        self.coords(self.hands['hour'], 150, 150, hour_x, hour_y)

        # Minute hand
        minute_x = 150 + 80 * math.cos(minute_angle)
        minute_y = 150 + 80 * math.sin(minute_angle)
        self.coords(self.hands['minute'], 150, 150, minute_x, minute_y)

        # Second hand
        second_x = 150 + 90 * math.cos(second_angle)
        second_y = 150 + 90 * math.sin(second_angle)
        self.coords(self.hands['second'], 150, 150, second_x, second_y)

        # Schedule next update
        self.after(1000, self.update_clock)

# Create main window
root = tk.Tk()
root.title("Analog Clock")
root.geometry("300x300")

# Create and pack the clock
clock = AnalogClock(root, width=300, height=300)
clock.pack(expand=True)

# Start the main loop
root.mainloop()
