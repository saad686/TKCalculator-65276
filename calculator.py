import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                messagebox.showerror("Math Error", "Cannot divide by zero.")
                return
            result = num1 / num2

        result_label.config(text=f"Result: {result:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")
root.resizable(False, False)

title_label = tk.Label(root, text="Simple Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

entry_frame = tk.Frame(root)
entry_frame.pack(pady=5)

num1_entry = tk.Entry(entry_frame, width=12, font=("Arial", 12))
num1_entry.grid(row=0, column=0, padx=5)

num2_entry = tk.Entry(entry_frame, width=12, font=("Arial", 12))
num2_entry.grid(row=0, column=1, padx=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="+", width=5, height=2, command=lambda: calculate("add"))
add_button.grid(row=0, column=0, padx=5, pady=5)

subtract_button = tk.Button(button_frame, text="-", width=5, height=2, command=lambda: calculate("subtract"))
subtract_button.grid(row=0, column=1, padx=5, pady=5)

multiply_button = tk.Button(button_frame, text="×", width=5, height=2, command=lambda: calculate("multiply"))
multiply_button.grid(row=0, column=2, padx=5, pady=5)

divide_button = tk.Button(button_frame, text="÷", width=5, height=2, command=lambda: calculate("divide"))
divide_button.grid(row=0, column=3, padx=5, pady=5)

result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
