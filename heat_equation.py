import tkinter as tk
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def solve_heat_equation():
    # Get the parameters from the user
    L = float(L_entry.get())
    T = float(T_entry.get())
    alpha = float(alpha_entry.get())
    Nx = int(Nx_entry.get())
    Nt = int(Nt_entry.get())
    u0 = float(u0_entry.get())
    uL = float(uL_entry.get())

    # Discretize the spatial and time domains
    dx = L / (Nx - 1)
    dt = T / (Nt - 1)
    x = np.linspace(0, L, Nx)
    t = np.linspace(0, T, Nt)

    # Initialize the solution array
    u = np.zeros((Nx, Nt))
    u[0, :] = u0
    u[-1, :] = uL

    # Time-stepping loop to solve the PDE
    for n in range(1, Nt):
        for i in range(1, Nx - 1):
            u[i, n] = u[i, n - 1] + alpha * dt / dx**2 * (u[i + 1, n - 1] - 2 * u[i, n - 1] + u[i - 1, n - 1])

    # Plot the solution
    fig = plt.figure(figsize=(5, 5))
    plt.imshow(u, extent=[0, T, 0, L], origin='lower',aspect='auto')
    plt.xlabel('t')
    plt.ylabel('x')
    plt.title('Solution of 1D heat equation')

    # Display the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Create the main window
root = tk.Tk()
root.title("1D Heat Equation Solver")

# Create labels and entries for the parameters
L_label = tk.Label(root, text="Length of the rod L:")
L_label.grid(row=0, column=0)
L_entry = tk.Entry(root)
L_entry.grid(row=0, column=1)

T_label = tk.Label(root, text="Total time T:")
T_label.grid(row=1, column=0)
T_entry = tk.Entry(root)
T_entry.grid(row=1, column=1)

alpha_label = tk.Label(root, text="Thermal diffusivity alpha:")
alpha_label.grid(row=2, column=0)
alpha_entry = tk.Entry(root)
alpha_entry.grid(row=2, column=1)

Nx_label = tk.Label(root, text="Number of spatial nodes Nx:")
Nx_label.grid(row=3, column=0)
Nx_entry = tk.Entry(root)
Nx_entry.grid(row=3, column=1)

Nt_label = tk.Label(root, text="Number of time steps Nt:")
Nt_label.grid(row=4, column=0)
Nt_entry = tk.Entry(root)
Nt_entry.grid(row=4, column=1)

u0_label = tk.Label(root, text="Initial temperature u(0,t):")
u0_label.grid(row=5, column=0)
u0_entry = tk.Entry(root)
u0_entry.grid(row=5, column=1)

uL_label = tk.Label(root, text="Temperature at x=L u(L,t):")
uL_label.grid(row=6, column=0)
uL_entry = tk.Entry(root)
uL_entry.grid(row=6, column=1)

solve_button = tk.Button(root, text="Solve PDE", command=solve_heat_equation)
solve_button.grid(row=7, column=0, columnspan=2)

root.mainloop()



