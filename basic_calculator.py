import tkinter as tk

def button_click(number):
    current = e.get()
    e.delete(0,tk.END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0,tk.END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0,tk.END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0,tk.END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0,tk.END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0,tk.END)

def button_equal():
    second_number = e.get()
    e.delete(0,tk.END)

    if math == "addition":
        e.insert(0, f_num + float(second_number))

    if math == "subtraction":
        e.insert(0, f_num - float(second_number))

    if math == "multiplication":
        e.insert(0, f_num * float(second_number))

    if math == "division":
        e.insert(0, f_num / float(second_number))

root = tk.Tk()
root.title("Calculator")

e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button
