import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FractalGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Fractal Generator")

        self.width_label = tk.Label(root, text="Width:")
        self.width_label.pack(side="left")

        self.width_entry = tk.Entry(root, width=10)
        self.width_entry.pack(side="left")
        self.width_entry.insert(0, "400")

        self.height_label = tk.Label(root, text="Height:")
        self.height_label.pack(side="left")

        self.height_entry = tk.Entry(root, width=10)
        self.height_entry.pack(side="left")
        self.height_entry.insert(0, "400")

        self.maxit_label = tk.Label(root, text="Max Iterations:")
        self.maxit_label.pack(side="left")

        self.maxit_entry = tk.Entry(root, width=10)
        self.maxit_entry.pack(side="left")
        self.maxit_entry.insert(0, "20")

        self.fractal_type_label = tk.Label(root, text="Fractal Type:")
        self.fractal_type_label.pack(side="left")

        self.fractal_type_var = tk.StringVar(root)
        self.fractal_type_var.set("Mandelbrot Set")
        self.fractal_type_menu = tk.OptionMenu(root, self.fractal_type_var, "Mandelbrot Set", "Julia Set", "Burning Ship")
        self.fractal_type_menu.pack(side="left")

        self.generate_button = tk.Button(root, text="Generate", command=self.generate_fractal)
        self.generate_button.pack(side="left")

        self.figure = plt.Figure(figsize=(5,5), dpi=100)
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, root)

    def mandelbrot(self, h, w, maxit=20):
        """
        Generate a Mandelbrot set
        :param h: Image height
        :param w: Image width
        :param maxit: Maximum number of iterations
        :return: 2D numpy array representing the fractal
        """
        xmin, xmax = -2.0, 1.0
        ymin, ymax = -1.5, 1.5
        mandelbrot = np.zeros((h, w))
        for x in range(w):
            for y in range(h):
                z = complex(0, 0)
                c = complex(x * (xmax - xmin) / (w - 1) + xmin, y * (ymax - ymin) / (h - 1) + ymin)
                iterations = 0
                while abs(z) <= 2 and iterations < maxit:
                    z = z * z + c
                    iterations += 1
                mandelbrot[y, x] = iterations
        return mandelbrot
    def generate_fractal(self):
        width = int(self.width_entry.get())
        height = int(self.height_entry.get())
        maxit = int(self.maxit_entry.get())
        fractal_type = self.fractal_type_var.get()

        if fractal_type == "Mandelbrot Set":
            self.axes.imshow(self.mandelbrot(height, width, maxit), cmap="hot")
        elif fractal_type == "Julia Set":
            self.axes.imshow(self.julia(height, width, maxit), cmap="hot")
        elif fractal_type == "Burning Ship":
            self.axes.imshow(self.burning_ship(height, width, maxit), cmap="hot")

        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="bottom", fill="both", expand=True)

    def julia(self, h, w, maxit=20):
        """
        Generate a Julia set
        :param h: Image height
        :param w: Image width
        :param maxit: Maximum number of iterations
        :return: 2D numpy array representing the fractal
        """
        c = complex(-0.8, 0.156)
        xmin, xmax = -1.5, 1.5
        ymin, ymax = -1.5, 1.5
        julia = np.zeros((h, w))
        for x in range(w):
            for y in range(h):
                z = complex(x * (xmax - xmin) / (w - 1) + xmin, y * (ymax - ymin) / (h - 1) + ymin)
                iterations = 0
                while abs(z) <= 2 and iterations < maxit:
                    z = z * z + c
                    iterations += 1
                julia[y, x] = iterations
        return julia

    def burning_ship(self, h, w, maxit=20):
        """
        Generate a Burning Ship fractal
        :param h: Image height
        :param w: Image width
        :param maxit: Maximum number of iterations
        :return: 2D numpy array representing the fractal
        """
        xmin, xmax = -2.0, 1.0
        ymin, ymax = -2.0, 2.0
        burning_ship = np.zeros((h, w))
        for x in range(w):
            for y in range(h):
                z = complex(x * (xmax - xmin) / (w - 1) + xmin, y * (ymax - ymin) / (h - 1) + ymin)
                c = z
                iterations = 0
                while abs(z) <= 2 and iterations < maxit:
                    z = complex(abs(z.real), abs(z.imag)) ** 2 + c
                    iterations += 1
                burning_ship[y, x] = iterations
        return burning_ship


if __name__ == "__main__":
    root = tk.Tk()
    fractal_generator = FractalGenerator(root)
    root.mainloop()
