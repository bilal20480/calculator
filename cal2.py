import tkinter as tk
import math
from tkinter import messagebox

# ----------------- Theme Colors -----------------
BG_COLOR = "#1e1e1e"
BTN_COLOR = "#292929"
HOVER_COLOR = "#3a3a3a"
ACTIVE_COLOR = "#505050"
TEXT_COLOR = "#ffffff"
FONT = ("Consolas", 18)

# ----------------- Expression Handler -----------------
expression = ""

def update_entry(value):
    global expression
    if value == "C":
        expression = ""
    elif value == "⌫":
        expression = expression[:-1]
    elif value == "=":
        try:
            result = str(eval(expression.replace("^", "**").replace("π", str(math.pi)).replace("e", str(math.e))))
            expression = result
        except:
            expression = ""
            status_label.config(text="Error!", fg="red")
            return
    else:
        expression += value
    entry_var.set(expression)
    status_label.config(text="")

def convert_to_func(txt):
    funcs = {
        "sin": "math.sin(",
        "cos": "math.cos(",
        "tan": "math.tan(",
        "log": "math.log10(",
        "sqrt": "math.sqrt(",
    }
    return funcs.get(txt, txt)

# ----------------- Hover Effects -----------------
def on_enter(e): e.widget.config(bg=HOVER_COLOR)
def on_leave(e): e.widget.config(bg=BTN_COLOR)

# ----------------- UI Setup -----------------
root = tk.Tk()
root.title("Interactive Scientific Calculator")
root.geometry("450x700")
root.config(bg=BG_COLOR)
root.resizable(False, False)

# ----------------- Entry Field -----------------
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Consolas", 24), bd=0,
                 bg="#101010", fg=TEXT_COLOR, insertbackground=TEXT_COLOR,
                 justify="right", relief="flat")
entry.pack(padx=20, pady=(30, 10), ipady=20, fill="both")

# ----------------- Status Label -----------------
status_label = tk.Label(root, text="", fg="green", bg=BG_COLOR, font=("Consolas", 12))
status_label.pack(pady=(0, 5))

# ----------------- Button Layout -----------------
button_rows = [
    ['C', '⌫', '(', ')'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['sin', 'cos', 'tan', '^'],
    ['log', 'sqrt', 'π', 'e']
]

btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.pack(padx=15, pady=10, fill="both", expand=True)

for row in button_rows:
    row_frame = tk.Frame(btn_frame, bg=BG_COLOR)
    row_frame.pack(expand=True, fill='both')
    for char in row:
        btn = tk.Button(row_frame, text=char, font=FONT, bg=BTN_COLOR, fg=TEXT_COLOR,
                        activebackground=ACTIVE_COLOR, activeforeground="white",
                        relief="flat", cursor="hand2", bd=0,
                        command=lambda txt=char: update_entry(convert_to_func(txt)))
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

# ----------------- Keyboard Bindings -----------------
def key_handler(event):
    key = event.char
    if key in "0123456789.+-*/()^":
        update_entry(key)
    elif key == "\r":  # Enter
        update_entry("=")
    elif key == "\x08":  # Backspace
        update_entry("⌫")
    elif key.lower() == "c":
        update_entry("C")

root.bind("<Key>", key_handler)

# ----------------- Run App -----------------
root.mainloop()
