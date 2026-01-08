import tkinter as tk

# Window
root = tk.Tk()
root.title("Newton's Laws of Motion")

canvas = tk.Canvas(root, width=800, height=300, bg="white")
canvas.pack()

# Variables
mass = 2          # mass of block
force = 0.5       # applied force
velocity = 0
position = 50
dt = 0.5

# Objects
ground = canvas.create_line(0, 200, 800, 200, width=2)
block = canvas.create_rectangle(position, 170, position + 60, 200, fill="blue")
text = canvas.create_text(400, 30, text="", font=("Arial", 12))

def animate():
    global velocity, position

    acceleration = force / mass   # Newton's Second Law
    velocity += acceleration * dt
    position += velocity * dt

    canvas.coords(block, position, 170, position + 60, 200)
    canvas.itemconfig(
        text,
        text=f"Force = {force} N    Mass = {mass} kg    Acceleration = {acceleration:.2f} m/s²"
    )

    if position < 740:
        root.after(50, animate)

animate()
root.mainloop()
