from dearpygui.dearpygui import *
add_text("Hello World Text")
add_button("Submit" , callback="submit_callback")
add_input_text("string")

def submit_callback(sender ,data):
    print("Submit Cicked")

start_dearpygui()

