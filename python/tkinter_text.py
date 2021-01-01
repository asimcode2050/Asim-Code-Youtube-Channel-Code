import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack()
canvas_t = canvas.create_text(10,10,text='',anchor=tk.NW)
our_text ="Hello from Asim Code"
delta = 500
delay = 0
for x in range(len(our_text)+1):
    s = our_text[:x]
    new_text = lambda s=s: canvas.itemconfigure(canvas_t,text=s)
    canvas.after(delay,new_text)
    delay += delta

root.mainloop()