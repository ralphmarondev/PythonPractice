import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S %p')
    time_label.config(text=current_time)
    greet_user()

def greet_user():
    current_hour = int(strftime('%H'))
    if 6 <= current_hour < 12:
        greeting = "Good Morning!"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"
    greeting_label.config(text=greeting)

app = tk.Tk()
app.title("Morning Greeting App")

time_label = tk.Label(app, font=('calibri', 40, 'bold'), background='black', foreground='white')
time_label.pack(anchor='center')

greeting_label = tk.Label(app, font=('calibri', 20, 'bold'), background='black', foreground='white')
greeting_label.pack(anchor='center')

update_time()

app.after(1000, update_time)  # Update time every 1000 milliseconds (1 second)

app.mainloop()
