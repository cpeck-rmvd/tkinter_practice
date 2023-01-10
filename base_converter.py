import tkinter as tk

def convert_base():
    input_number = input_entry.get()
    from_base = int(from_base_entry.get())
    to_base = int(to_base_entry.get())
    try:
        decimal_number = int(str(input_number), from_base)
        new_number = str(hex(decimal_number))[2:].upper()
        if to_base == 16:
            output_label.config(text=new_number)
        elif to_base == 10:
            output_label.config(text=str(int(new_number, 16)))
        else:
            output_label.config(text=str(int(new_number, 16), to_base))
    except ValueError:
        output_label.config(text="Invalid input.")

root = tk.Tk()
root.title("Base Converter")

input_label = tk.Label(root, text="Input number:")
input_label.grid(row=0, column=0)
input_entry = tk.Entry(root)
input_entry.grid(row=0, column=1)

from_base_label = tk.Label(root, text="From base:")
from_base_label.grid(row=1, column=0)
from_base_entry = tk.Entry(root)
from_base_entry.grid(row=1, column=1)

to_base_label = tk.Label(root, text="To base:")
to_base_label.grid(row=2, column=0)
to_base_entry = tk.Entry(root)
to_base_entry.grid(row=2, column=1)

convert_button = tk.Button(root, text="Convert", command=convert_base)
convert_button.grid(row=3, column=0, columnspan=2)

output_label = tk.Label(root, text="")
output_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
