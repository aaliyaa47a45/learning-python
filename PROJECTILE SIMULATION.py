import tkinter as tk
import math
import time

# Create window
root = tk.Tk()
root.title("Projectile Motion Simulation")
root.geometry("800x500")

# Canvas
canvas = tk.Canvas(root, width=800, height=400, bg="white")
canvas.pack()

# Inputs
frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Velocity (m/s):").grid(row=0, column=0)
velocity_entry = tk.Entry(frame)
velocity_entry.grid(row=0, column=1)

tk.Label(frame, text="Angle (degrees):").grid(row=1, column=0)
angle_entry = tk.Entry(frame)
angle_entry.grid(row=1, column=1)

g = 9.8

def simulate():
    canvas.delete("all")

    u = float(velocity_entry.get())
    angle = float(angle_entry.get())

    theta = math.radians(angle)

    x = 50
    y = 350
    t = 0
    dt = 0.1

    ball = canvas.create_oval(x, y, x+10, y+10, fill="red")

    while y < 400:
        x = 50 + u * math.cos(theta) * t * 5
        y = 350 - (u * math.sin(theta) * t - 0.5 * g * t * t) * 5

        canvas.coords(ball, x, y, x+10, y+10)
        root.update()
        time.sleep(0.02)

        t += dt

# Button
tk.Button(root, text="Start Simulation", command=simulate).pack(pady=10)

root.mainloop()
