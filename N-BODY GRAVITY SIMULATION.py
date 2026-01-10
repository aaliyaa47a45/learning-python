import tkinter as tk
import math
import random

# Window
root = tk.Tk()
root.title("N-Body Gravitational Simulation")

canvas = tk.Canvas(root, width=700, height=700, bg="black")
canvas.pack()

G = 1        # scaled gravitational constant
dt = 0.5

class Body:
    def _init_(self, x, y, vx, vy, mass, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.id = canvas.create_oval(
            x-5, y-5, x+5, y+5, fill=color
        )

bodies = [
    Body(350, 350, 0, 0, 5000, "yellow"),   # star
    Body(350, 200, 4, 0, 10, "white"),      # planet 1
    Body(350, 120, 3, 0, 8, "blue"),        # planet 2
    Body(350, 80, 2.5, 0, 6, "red")          # planet 3
]

def animate():
    for i in range(len(bodies)):
        fx = fy = 0
        for j in range(len(bodies)):
            if i != j:
                dx = bodies[j].x - bodies[i].x
                dy = bodies[j].y - bodies[i].y
                r = math.sqrt(dx*dx + dy*dy) + 0.1
                f = G * bodies[i].mass * bodies[j].mass / (r*r)
                fx += f * dx / r
                fy += f * dy / r

        # Acceleration
        bodies[i].vx += fx / bodies[i].mass * dt
        bodies[i].vy += fy / bodies[i].mass * dt

    # Update positions
    for b in bodies:
        b.x += b.vx * dt
        b.y += b.vy * dt
        canvas.coords(b.id, b.x-5, b.y-5, b.x+5, b.y+5)

    root.after(20, animate)

animate()
root.mainloop()
