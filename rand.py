import tkinter as tk
from tkinter import ttk
from random import randint

def generate_random_number():
    result_label.config(text="")
    try:
        min_value = int(min_range_combobox.get())
        max_value = int(max_range_combobox.get())

        if min_value >= max_value:
            result_label.config(text="Be sure that min_value < max_value")
        else:
            random_number = randint(min_value, max_value)
            result_label.config(text=f"Result: {random_number}")
    except Exception as e:
        result_label.config(text=str(e))

root = tk.Tk()
root.title("Random generator")

min_label = tk.Label(root, text="Min value:")
min_label.pack(pady=5)

min_range_combobox = ttk.Combobox(root, values=list(range(0, 101)), width=10)
min_range_combobox.set("0")  
min_range_combobox.pack()

max_label = tk.Label(root, text="Max value:")
max_label.pack(pady=5)

max_range_combobox = ttk.Combobox(root, values=list(range(0, 101)), width=10)
max_range_combobox.set("100")  
max_range_combobox.pack()


generate_button = tk.Button(root, text="Generate", command=generate_random_number)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="Press to generate random number")
result_label.pack(pady=10)

root.mainloop()
