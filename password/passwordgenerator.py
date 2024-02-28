import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""
    meets_criteria = False
    has_number = False
    has_special = False



    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return password

def generate_password_and_display():
    min_length = int(length_entry.get())
    has_number = number_var.get()
    has_special = special_var.get()
    password = generate_password(min_length, has_number, has_special)
    password_display.config(text=password)

#main window
root = tk.Tk()
root.title("Password Generator")

# Create and pack widgets
length_label = ttk.Label(root, text="Minimum Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = ttk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)

number_var = tk.BooleanVar()
number_checkbox = ttk.Checkbutton(root, text="Include Numbers", variable=number_var)
number_checkbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="w")

special_var = tk.BooleanVar()
special_checkbox = ttk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_checkbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")

generate_button = ttk.Button(root, text="Generate Password", command=generate_password_and_display)
generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

password_display = ttk.Label(root, text="")
password_display.grid(row=4, column=0, columnspan=2, padx=5, pady=5)


root.mainloop()
