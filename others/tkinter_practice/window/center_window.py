# center the window on the screen
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Maron Cute - [center of screen]")

    window_width = 500
    window_height = 300

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_width / 2)

    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    width = 500
    height = 300
    root.minsize(width, height)
    root.maxsize(width * 2, height * 2)

    #root.resizable(False, False)

    # transparency
    # using alpha channel from 0.0 [fully transparent] to 1.0 [fully opaque]
    # root.attributes('-alpha', 0.5)

    # to make the window always on top
    root.attributes('-topmost', 1)

    # move the window up or down of the window stacking order
    root.lift()
    root.lower()

    # change default icon
    # root.iconbitmap('./../../res/icon.jpg')

    root.mainloop()
