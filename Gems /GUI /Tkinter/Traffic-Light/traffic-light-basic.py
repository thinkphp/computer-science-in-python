import tkinter as tk

class TrafficLight:
    def __init__(self, canvas, x_offset, y_offset):
        self.canvas = canvas
        self.x_offset = x_offset
        self.y_offset = y_offset

        # Draw three circles for the traffic light
        self.red_light = self.canvas.create_oval(20 + self.x_offset, 40 + self.y_offset, 120 + self.x_offset, 140 + self.y_offset, fill="gray")
        self.yellow_light = self.canvas.create_oval(20 + self.x_offset, 160 + self.y_offset, 120 + self.x_offset, 260 + self.y_offset, fill="gray")
        self.green_light = self.canvas.create_oval(20 + self.x_offset, 280 + self.y_offset, 120 + self.x_offset, 380 + self.y_offset, fill="gray")

    def set_color(self, red, yellow, green):
        # Update the colors of the lights
        self.canvas.itemconfig(self.red_light, fill=red)
        self.canvas.itemconfig(self.yellow_light, fill=yellow)
        self.canvas.itemconfig(self.green_light, fill=green)

class TrafficSimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Light Simulation")
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()

        # Create labels above the traffic lights
        self.canvas.create_text(100, 30, text="Pedestrian", font=("Arial", 17, "bold"))
        self.canvas.create_text(350, 30, text="Car Light", font=("Arial", 17, "bold"))

        # Create two traffic lights: one for pedestrians, one for cars
        self.pedestrian_light = TrafficLight(self.canvas, 50, 50)
        self.car_light = TrafficLight(self.canvas, 300, 50)

        # Start the simulation
        self.current_state = 0
        self.update_lights()

    def update_lights(self):
        # Cycle between the traffic light states
        if self.current_state == 0:
            # Green for pedestrians, Red for cars
            self.pedestrian_light.set_color("gray", "gray", "green")
            self.car_light.set_color("red", "gray", "gray")
            self.current_state = 1
        elif self.current_state == 1:
            # Yellow for pedestrians, Red for cars
            self.pedestrian_light.set_color("gray", "yellow", "gray")
            self.car_light.set_color("red", "gray", "gray")
            self.current_state = 2
        elif self.current_state == 2:
            # Red for pedestrians, Green for cars
            self.pedestrian_light.set_color("red", "gray", "gray")
            self.car_light.set_color("gray", "gray", "green")
            self.current_state = 3
        elif self.current_state == 3:
            # Red for pedestrians, Yellow for cars
            self.pedestrian_light.set_color("red", "gray", "gray")
            self.car_light.set_color("gray", "yellow", "gray")
            self.current_state = 0

        # Update the lights every 2 seconds
        self.root.after(2000, self.update_lights)

# Initialize the main application window
root = tk.Tk()
app = TrafficSimulation(root)
root.mainloop()
