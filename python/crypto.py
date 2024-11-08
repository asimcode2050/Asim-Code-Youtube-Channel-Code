import tkinter as tk
from tkinter import messagebox
import requests


def get_conversion_rates():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,ripple,litecoin&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching data: {str(e)}")
        return None


def convert():
    amount = entry_amount.get()
    from_currency = combo_from_currency.get()
    to_currency = combo_to_currency.get()
    if not amount or not from_currency or not to_currency:
        messagebox.showerror("Input Error", "Please fill all fields.")
        return
    try:
        amount = float(amount)
        if amount <= 0:
            messagebox.showerror(
                "Input Error", "Amount must be a positive number.")
            return
    except ValueError:
        messagebox.showerror(
            "Input Error", "Please enter a valid number for amount.")
        return
    rates = get_conversion_rates()
    if rates is None:
        return
    try:
        from_rate = rates[from_currency.lower()]["usd"]
        to_rate = rates[to_currency.lower()]["usd"]
    except KeyError:
        messagebox.showerror("Error", "Invalid currency selected.")
        return
    converted_amount = (amount / from_rate) * to_rate
    result_label.config(text=f"{amount} {from_currency} = {
                        converted_amount:.6f} {to_currency}")


root = tk.Tk()
root.title("Cryptocurrency Converter")
root.geometry("500x500")

label_title = tk.Label(
    root, text="Cryptocurrency Converter", font=("Helvetica", 16))
label_title.pack(pady=10)
label_amount = tk.Label(root, text="Amount:")
label_amount.pack(pady=5)
entry_amount = tk.Entry(root)
entry_amount.pack(pady=5)

label_from_currency = tk.Label(root, text="From Currency:")
label_from_currency.pack(pady=5)
combo_from_currency = tk.StringVar(root)
combo_from_currency.set("Bitcoin")  # default value
dropdown_from = tk.OptionMenu(
    root, combo_from_currency, "Bitcoin", "Ethereum", "Ripple", "Litecoin")
dropdown_from.pack(pady=5)
label_to_currency = tk.Label(root, text="To Currency:")
label_to_currency.pack(pady=5)
combo_to_currency = tk.StringVar(root)
combo_to_currency.set("Ethereum")  # default value
dropdown_to = tk.OptionMenu(root, combo_to_currency,
                            "Bitcoin", "Ethereum", "Ripple", "Litecoin")
dropdown_to.pack(pady=5)
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=20)
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)
root.mainloop()
