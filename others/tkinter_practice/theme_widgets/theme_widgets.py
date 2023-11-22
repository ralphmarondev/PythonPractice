import tkinter as tk
from tkinter import ttk

if __name__ == '__main__':
    root = tk.Tk()

    tk.Label(root, text="Classic Label").pack()
    ttk.Label(root, text="Themed Label").pack()

    root.mainloop()
   