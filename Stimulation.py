import tkinter as tk

g=9.8
t=0

root = tk.Tk()
root.title("Free Fall Stimulation")

canvas = tk.Canvas(root,width=400,height=500)
canvas.pack()

ball= canvas.create_oval(190,20,210,40,fill="green")

def fall():
    global t
    y= 20+0.5*g*t*t
    if y<460:
        canvas.coords(ball,190,y,210,y+20)
        t+=0.2
        root.after(50,fall)

fall()
root.mainloop()
