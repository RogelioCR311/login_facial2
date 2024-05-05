import tkinter as tk
from tkinter import ttk

def on_checkbox_toggle():
    if check_var.get():
        entry_var.set("True")
    else:
        entry_var.set("False")

root = tk.Tk()

entry_var = tk.StringVar()
entry = ttk.Entry(root, textvariable=entry_var)
entry.pack()

check_var = tk.BooleanVar()
checkbox = ttk.Checkbutton(root, text="Check", variable=check_var, command=on_checkbox_toggle)
checkbox.pack()

root.mainloop()
