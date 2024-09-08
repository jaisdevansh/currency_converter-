from currency_converter import CurrencyConverter
import tkinter as tk
from tkinter import messagebox

# Initialize CurrencyConverter
a = CurrencyConverter()

# Create a window
window = tk.Tk()
window.title("Currency Converter")
window.geometry("500x400")

# Function to handle conversion
def convert_currency():
    try:
        amount = float(e1.get())
        curr1 = e2.get().upper()
        curr2 = e3.get().upper()
        data = a.convert(amount, curr1, curr2)
        l5.config(text=f"Converted Amount: {data:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount.")
    except Exception as e:
        messagebox.showerror("Conversion Error", str(e))

# Function to clear input fields
def clear_fields():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    l5.config(text="")

# Function to swap currencies
def swap_currencies():
    curr1 = e2.get()
    curr2 = e3.get()
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e2.insert(0, curr2)
    e3.insert(0, curr1)

# Labels and Entries
l1 = tk.Label(window, text="Currency Converter", font="Times 20 bold")
l2 = tk.Label(window, text="Enter the amount:", font="Times 15 bold")
e1 = tk.Entry(window)
l3 = tk.Label(window, text="Source currency:", font="Times 15 bold")
e2 = tk.Entry(window)
l4 = tk.Label(window, text="Target currency:", font="Times 15 bold")
e3 = tk.Entry(window)
b1 = tk.Button(window, text="Convert", command=convert_currency)
b2 = tk.Button(window, text="Clear", command=clear_fields)
b3 = tk.Button(window, text="Swap", command=swap_currencies)
l5 = tk.Label(window, text="", font="Times 15 bold")

# Placing widgets in the window
l1.place(x=100, y=50)
l2.place(x=50, y=80)
e1.place(x=270, y=87)
l3.place(x=50, y=120)
e2.place(x=270, y=125)
l4.place(x=50, y=160)
e3.place(x=270, y=163)
b1.place(x=150, y=240)
b2.place(x=220, y=240)
b3.place(x=290, y=240)
l5.place(x=150, y=280)

# Run the main event loop
window.mainloop()
