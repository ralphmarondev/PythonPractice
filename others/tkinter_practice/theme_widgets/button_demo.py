import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import  showinfo

def show_button_click():
    showinfo(
        title="Information",
        message="Ralph Maron is cute"
    )

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("300x200")
    root.resizable(False, False)
    root.title("Button Demo")

    # show button
    show_button = ttk.Button(
        root,
        text="Show",
        command=show_button_click
    )

    show_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    # exit button
    exit_button = ttk.Button(
        root,
        text="Exit",
        command=lambda : root.quit()
    )

    exit_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )


    root.mainloop()
