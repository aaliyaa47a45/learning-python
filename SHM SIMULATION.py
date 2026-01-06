import tkinter as tk
import math
import time

# Window
root = tk.Tk()
root.title("Simple Harmonic Motion Simulation")

WIDTH, HEIGHT = 800, 300
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# Parameters
A = 150        # Amplitude
k = 0.05       # Spring constant
m = 1          # Mass
omega = math.sqrt(k / m)
t = 0

center_x = WIDTH // 2
center_y = HEIGHT // 2

# Objects
spring = canvas.create_line(0, center_y, center_x, center_y, width=3)
block = canvas.create_rectangle(0, 0, 0, 0, fill="blue")

def update():
    global t
    t += 0.1

    # SHM equation
    x = A * math.cos(omega * t)

    block_x = center_x + x

    # Update spring
    canvas.coords(spring, 50, center_y, block_x - 20, center_y)

    # Update block
    canvas.coords(
        block,
        block_x - 20, center_y - 20,
        block_x + 20, center_y + 20
    )

    root.after(30, update)

update()
root.mainloop()
