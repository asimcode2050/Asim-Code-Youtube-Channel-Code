import tkinter as tk
import time

class Demo():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_timer()
        self.root.mainloop()

    def update_timer(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000,self.update_timer)

app = Demo()

