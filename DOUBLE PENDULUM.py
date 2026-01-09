import tkinter as tk
import math

# Window
root = tk.Tk()
root.title("Double Pendulum Simulation (Chaos)")

canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

# Constants
g = 9.8
L1 = 150
L2 = 150
m1 = 10
m2 = 10
dt = 0.05

# Initial angles
theta1 = math.pi / 2
theta2 = math.pi / 2
omega1 = 0
omega2 = 0

origin_x = 300
origin_y = 150

# Objects
rod1 = canvas.create_line(0, 0, 0, 0, width=3)
rod2 = canvas.create_line(0, 0, 0, 0, width=3)
bob1 = canvas.create_oval(0, 0, 0, 0, fill="red")
bob2 = canvas.create_oval(0, 0, 0, 0, fill="blue")

def animate():
    global theta1, theta2, omega1, omega2

    # Equations of motion
    num1 = -g * (2*m1 + m2) * math.sin(theta1)
    num2 = -m2 * g * math.sin(theta1 - 2*theta2)
    num3 = -2 * math.sin(theta1 - theta2) * m2
    num4 = omega2*2 * L2 + omega1*2 * L1 * math.cos(theta1 - theta2)
    den = L1 * (2*m1 + m2 - m2 * math.cos(2*theta1 - 2*theta2))
    alpha1 = (num1 + num2 + num3 * num4) / den

    num1 = 2 * math.sin(theta1 - theta2)
    num2 = omega1**2 * L1 * (m1 + m2)
    num3 = g * (m1 + m2) * math.cos(theta1)
    num4 = omega2**2 * L2 * m2 * math.cos(theta1 - theta2)
    den = L2 * (2*m1 + m2 - m2 * math.cos(2*theta1 - 2*theta2))
    alpha2 = (num1 * (num2 + num3 + num4)) / den

    # Update velocities
    omega1 += alpha1 * dt
    omega2 += alpha2 * dt

    # Update angles
    theta1 += omega1 * dt
    theta2 += omega2 * dt

    # Positions
    x1 = origin_x + L1 * math.sin(theta1)
    y1 = origin_y + L1 * math.cos(theta1)

    x2 = x1 + L2 * math.sin(theta2)
    y2 = y1 + L2 * math.cos(theta2)

    # Draw
    canvas.coords(rod1, origin_x, origin_y, x1, y1)
    canvas.coords(rod2, x1, y1, x2, y2)

    canvas.coords(bob1, x1-8, y1-8, x1+8, y1+8)
    canvas.coords(bob2, x2-8, y2-8, x2+8, y2+8)

    root.after(20, animate)

animate()
root.mainloop()
