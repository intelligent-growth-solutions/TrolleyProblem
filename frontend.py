import time
import tkinter as tk
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Frontend:
    def __init__(self, root):
        if root is not None:
            self.root = root
            self.root.title("Tkinter UI with Matplotlib")
        else:
            self.root = None

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 100)

    def plot_point(self, x, y):
        self.root.title("we made it")
        #self.clear_plot()
        print("Plotting point:", x, y)
        #self.ax.plot(x, y, 'ro')
        self.ax.scatter(x, y, color='red', zorder=5)
        self.canvas.draw()

    def clear_plot(self):
        self.ax.clear()
        self.canvas.draw()

def run_ui(ui_pipe):
    root = tk.Tk()
    app = Frontend(root)

    # Receive messages from the pipe and plot points
    while True:
        if ui_pipe.poll():
            x, y = ui_pipe.recv()
            app.plot_point(x, y)
        else:
            root.update()  # Update the Tkinter event loop
            time.sleep(0.1)  # Add a short delay to avoid busy waiting

    root.mainloop()


