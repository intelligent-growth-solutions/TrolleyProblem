import tkinter as tk
from tkinter import messagebox
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pynput import mouse

def on_move(x, y):
    inverted_y = screen_height - y
    label.config(text=f"Cursor Position - X: {x}, Y: {inverted_y}")
    update_plot(x, inverted_y)

def update_plot(x, y):
    ax.clear()
    ax.scatter(x, y, color='red')
    ax.set_xlim(0, screen_width)
    ax.set_ylim(0, screen_height)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Plot of Cursor Position')
    canvas.draw()

# Create the main window
root = tk.Tk()
root.title("Real-Time Cursor Position")

# Get screen resolution
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Create a label to display cursor position
label = tk.Label(root, text="Cursor Position - X: 0, Y: 0")
label.pack(padx=10, pady=10)

# Create a matplotlib figure and subplot
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Bind mouse motion event to the canvas
listener = mouse.Listener(on_move=on_move)
listener.start()

# Run the application
root.mainloop()
