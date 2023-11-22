import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Ralph Maron is cute!")

    #region  GEOMETRY
    # width * height +- x +- y
    # root.geometry("300x200+50+50")
    # get screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = 300
    window_height = 200

    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    #endregion GEOMETRY

    root.mainloop()
