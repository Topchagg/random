import tkinter as tk
from tkinter import ttk
from random import randint

def generate_random_number():
    try:
        min_value = int(min_range_combobox.get())
        max_value = int(max_range_combobox.get())
        
        if min_value >= max_value:
            result_label.config(text="min value higher than max value")
            return
        
        ignored_value = None
        if ignore_listbox.curselection():
            ignored_value = int(ignore_listbox.get(ignore_listbox.curselection()[0]))
        
        random_number = randint(min_value,max_value)
        if not ignored_value:
            result_label.config(text=f"Result: {random_number}")
        else:
            attemps = 0
            while attemps < 20:
                attemps += 1
                if random_number != ignored_value:
                    result_label.config(text=f"Result: {random_number}")
                    break
                random_number = randint(min_value,max_value)
            return
    except Exception as e:
        result_label.config(text=str(e))

def add_ignore_value():
    try:
        value = int(ignore_entry.get())
        ignore_listbox.delete(0, tk.END)
        ignore_listbox.insert(tk.END, value)
        ignore_entry.delete(0, tk.END)
    except Exception as e:
        result_label.config(text=str(e))

def remove_ignore_value():
    ignore_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("Generator of random numbers")

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

ignore_label = tk.Label(root, text="Add ignored value:")
ignore_label.pack(pady=5)

ignore_entry = tk.Entry(root, width=15)
ignore_entry.pack()

add_ignore_button = tk.Button(root, text="Add", command=add_ignore_value)
add_ignore_button.pack(pady=5)

ignore_listbox = tk.Listbox(root, height=1, selectmode=tk.BROWSE)
ignore_listbox.pack()

remove_ignore_button = tk.Button(root, text="Clear ignored value", command=remove_ignore_value)
remove_ignore_button.pack(pady=5)

generate_button = tk.Button(root, text="Generate number", command=generate_random_number)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="Press to generate random number")
result_label.pack(pady=10)

root.mainloop()
