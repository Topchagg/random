import tkinter as tk
import random

def generate_random_number():
    random_number = random.randint(1, 100)
    result_label.config(text=f"Result: {random_number}")

root = tk.Tk()
root.title("Renerator of random nubmers")

generate_button = tk.Button(root, text="Generate number", command=generate_random_number)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="Press to generate random number")
result_label.pack(pady=10)

root.mainloop()
