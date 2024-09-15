import tkinter as tk
import time
import threading

class TrafficLight:
    def __init__(self, canvas, x, y, is_horizontal=True):
        self.canvas = canvas
        if is_horizontal:
            self.red = canvas.create_oval(x, y, x+30, y+30, fill="gray")
            self.yellow = canvas.create_oval(x+40, y, x+70, y+30, fill="gray")
            self.green = canvas.create_oval(x+80, y, x+110, y+30, fill="gray")
        else:
            self.red = canvas.create_oval(x, y, x+30, y+30, fill="gray")
            self.yellow = canvas.create_oval(x, y+40, x+30, y+70, fill="gray")
            self.green = canvas.create_oval(x, y+80, x+30, y+110, fill="gray")

    def set_color(self, color):
        self.canvas.itemconfig(self.red, fill="gray")
        self.canvas.itemconfig(self.yellow, fill="gray")
        self.canvas.itemconfig(self.green, fill="gray")
        if color == "red":
            self.canvas.itemconfig(self.red, fill="red")
        elif color == "yellow":
            self.canvas.itemconfig(self.yellow, fill="yellow")
        elif color == "green":
            self.canvas.itemconfig(self.green, fill="green")

class TrafficLightSimulation:
    def __init__(self, master):
        self.master = master
        self.master.title("Street Intersection Traffic Light Simulation")
        
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        # Draw street
        self.canvas.create_rectangle(150, 0, 250, 400, fill="gray")  # Vertical street
        self.canvas.create_rectangle(0, 150, 400, 250, fill="gray")  # Horizontal street

        # Traffic lights
        self.car_light = TrafficLight(self.canvas, 260, 50, is_horizontal=False)
        self.pedestrian_light = TrafficLight(self.canvas, 50, 260, is_horizontal=True)

        # Labels
        self.canvas.create_text(320, 100, text="Cars", font=("Arial", 12))
        self.canvas.create_text(100, 320, text="Pedestrians", font=("Arial", 12))

        # Car and pedestrian
        self.car = self.canvas.create_rectangle(175, 0, 225, 50, fill="blue")
        self.pedestrian = self.canvas.create_oval(0, 175, 25, 225, fill="yellow")

        # Start the simulation
        self.is_running = True
        threading.Thread(target=self.run_simulation, daemon=True).start()

    def run_simulation(self):
        while self.is_running:
            # Green for cars, red for pedestrians
            self.car_light.set_color("green")
            self.pedestrian_light.set_color("red")
            self.move_car()
            time.sleep(5)

            # Yellow for cars
            self.car_light.set_color("yellow")
            time.sleep(2)

            # Red for cars, green for pedestrians
            self.car_light.set_color("red")
            self.pedestrian_light.set_color("green")
            self.move_pedestrian()
            time.sleep(5)

            # Yellow for pedestrians (if applicable)
            self.pedestrian_light.set_color("yellow")
            time.sleep(2)

    def move_car(self):
        for _ in range(50):
            if not self.is_running:
                break
            self.canvas.move(self.car, 0, 4)
            self.master.update()
            time.sleep(0.05)
        self.canvas.moveto(self.car, 175, 0)

    def move_pedestrian(self):
        for _ in range(50):
            if not self.is_running:
                break
            self.canvas.move(self.pedestrian, 4, 0)
            self.master.update()
            time.sleep(0.05)
        self.canvas.moveto(self.pedestrian, 0, 175)

    def stop(self):
        self.is_running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficLightSimulation(root)
    root.protocol("WM_DELETE_WINDOW", app.stop)
    root.mainloop()
