import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graph_equation():
    # Get the equation from the user
    equation = equation_entry.get()

    # Create the x and y data for the graph
    x = np.linspace(-10, 10, 1000)
    y = eval(equation)

    # Create the graph
    fig = plt.figure(figsize=(5, 5))
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of y = {}'.format(equation))

    # Display the graph in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Create the main window
root = tk.Tk()
root.title("2-Variable Equation Grapher")

# Create a label and entry for the equation
equation_label = tk.Label(root, text="Enter an equation in terms of x and y")
equation_label.pack()
equation_entry = tk.Entry(root)
equation_entry.pack()

# Create a button to graph the equation
graph_button = tk.Button(root, text="Graph Equation", command=graph_equation)
graph_button.pack()

# Run the Tkinter event loop
root.mainloop()
