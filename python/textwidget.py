import tkinter as tk
from tkinter import ttk
gui  = tk.Tk()
gui.title('Textbox widget')
label = ttk.Label(gui, text="Our Label")
label.grid(column=0, row=0)
def button_click():
    action.configure(text='Hello '+ name.get()) 
ttk.Label(gui,text="Please enter your name:").grid(column=0, row=0)
name = tk.StringVar()
user_entry = ttk.Entry(gui,width=15, textvariable=name)
user_entry.grid(column=0, row=1)
action = ttk.Button(gui, text="Click",command=button_click)
action.grid(column=1,row=1)
gui.mainloop()