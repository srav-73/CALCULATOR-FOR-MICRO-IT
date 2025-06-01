import tkinter as tk

def press_button(value):
    entry.insert(tk.END, value)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear_entry():
    entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry widget
entry = tk.Entry(root, width=20, font=('Arial', 15), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Add buttons to the window
for text, row, col in buttons:
    tk.Button(root, text=text, width=6, height=2, font=('Arial', 12),
              command=lambda t=text: press_button(t) if t != '=' else evaluate()).grid(row=row, column=col)

# Clear button
tk.Button(root, text="Clear", width=14, height=2, font=('Arial', 12), command=clear_entry).grid(row=5, column=0, columnspan=2)

# Run the application
root.mainloop()
