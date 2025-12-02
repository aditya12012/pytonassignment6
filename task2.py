import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("330x470")
root.resizable(False, False)
root.configure(bg="#222")

expression = ""

# Update display
def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

# Clear display
def clear():
    global expression
    expression = ""
    input_text.set("")

# Evaluate expression safely
def equal():
    global expression
    try:
        if expression.strip() == "":
            messagebox.showwarning("Warning", "Nothing to calculate!")
            return

        result = str(eval(expression))
        input_text.set(result)
        expression = result  # allow further calculations

    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
        expression = ""
        input_text.set("")
    except Exception:
        messagebox.showerror("Error", "Invalid input!")
        expression = ""
        input_text.set("")


# Display field
input_text = tk.StringVar()
input_frame = tk.Frame(root, width=312, height=50, bd=0, bg="#333")
input_frame.pack()

input_field = tk.Entry(
    input_frame,
    font=('arial', 20, 'bold'),
    textvariable=input_text,
    width=25,
    bg="#eee",
    fg="#000",
    bd=0,
    justify="right"
)
input_field.grid(row=0, column=0)
input_field.pack(ipady=15)

# Buttons frame
btns_frame = tk.Frame(root, width=312, height=272.5, bg="#222")
btns_frame.pack()

# Row 1
tk.Button(btns_frame, text="C", fg="white", bg="#ff5252", width=32, height=3, command=clear).grid(row=0, column=0, columnspan=3)
tk.Button(btns_frame, text="/", fg="white", bg="#ff9800", width=10, height=3, command=lambda: press("/")).grid(row=0, column=3)

# Row 2
tk.Button(btns_frame, text="7", fg="white", bg="#333", width=10, height=3, command=lambda: press("7")).grid(row=1, column=0)
tk.Button(btns_frame, text="8", fg="white", bg="#333", width=10, height=3, command=lambda: press("8")).grid(row=1, column=1)
tk.Button(btns_frame, text="9", fg="white", bg="#333", width=10, height=3, command=lambda: press("9")).grid(row=1, column=2)
tk.Button(btns_frame, text="*", fg="white", bg="#ff9800", width=10, height=3, command=lambda: press("*")).grid(row=1, column=3)

# Row 3
tk.Button(btns_frame, text="4", fg="white", bg="#333", width=10, height=3, command=lambda: press("4")).grid(row=2, column=0)
tk.Button(btns_frame, text="5", fg="white", bg="#333", width=10, height=3, command=lambda: press("5")).grid(row=2, column=1)
tk.Button(btns_frame, text="6", fg="white", bg="#333", width=10, height=3, command=lambda: press("6")).grid(row=2, column=2)
tk.Button(btns_frame, text="-", fg="white", bg="#ff9800", width=10, height=3, command=lambda: press("-")).grid(row=2, column=3)

# Row 4
tk.Button(btns_frame, text="1", fg="white", bg="#333", width=10, height=3, command=lambda: press("1")).grid(row=3, column=0)
tk.Button(btns_frame, text="2", fg="white", bg="#333", width=10, height=3, command=lambda: press("2")).grid(row=3, column=1)
tk.Button(btns_frame, text="3", fg="white", bg="#333", width=10, height=3, command=lambda: press("3")).grid(row=3, column=2)
tk.Button(btns_frame, text="+", fg="white", bg="#ff9800", width=10, height=3, command=lambda: press("+")).grid(row=3, column=3)

# Row 5
tk.Button(btns_frame, text="0", fg="white", bg="#333", width=21, height=3, command=lambda: press("0")).grid(row=4, column=0, columnspan=2)
tk.Button(btns_frame, text=".", fg="white", bg="#333", width=10, height=3, command=lambda: press(".")).grid(row=4, column=2)
tk.Button(btns_frame, text="=", fg="white", bg="#4caf50", width=10, height=3, command=equal).grid(row=4, column=3)

root.mainloop()
