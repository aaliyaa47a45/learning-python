import tkinter as tk
import math

# Window
root = tk.Tk()
root.title("Wave Motion Simulation")

canvas = tk.Canvas(root, width=800, height=300, bg="white")
canvas.pack()

# Wave parameters
amplitude = 40
wavelength = 100
speed = 0.1
time = 0

def animate():
    global time
    canvas.delete("wave")

    for x in range(0, 800, 5):
        y = 150 + amplitude * math.sin((2 * math.pi / wavelength) * x - time)
        canvas.create_oval(x, y, x+2, y+2, fill="blue", tag="wave")

    time += speed
    root.after(30, animate)

animate()
root.mainloop()
