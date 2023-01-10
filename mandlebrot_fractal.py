import tkinter as tk
import numpy as np
from PIL import Image, ImageTk

def create_fractal():
    # Create an empty image with a white background
    width, height = 800, 800
    image = Image.new("RGB", (width, height), "white")
    pixels = image.load()
    # Define the properties of the fractal
    xmin, xmax = -2.0, 1.0
    ymin, ymax = -1.5, 1.5
    max_iter = 256
    # Generate the fractal
    for x in range(width):
        for y in range(height):
            zx, zy = x * (xmax - xmin) / (width - 1) + xmin, y * (ymax - ymin) / (height - 1) + ymin
            c = zx + zy * 1j
            z = c
            for i in range(max_iter):
                if abs(z) > 2.0:
                    break 
                z = z * z + c
            # Color the pixel based on the number of iterations
            r, g, b = i % 8 * 32, i % 16 * 16, i % 32 * 8
            pixels[x, y] = (r, g, b)

    # Convert the image to a PhotoImage object for Tkinter
    img = ImageTk.PhotoImage(image)
    # Create a label to display the fractal
    label = tk.Label(root, image=img)
    label.pack()

# Create the main window
root = tk.Tk()
root.title("Mandelbrot Fractal")

# Create a button to generate the fractal
button = tk.Button(root, text="Create Fractal", command=create_fractal)
button.pack()
root.mainloop()
