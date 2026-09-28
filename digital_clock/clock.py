import tkinter as tk
from time import strftime


def update_time():
    current_time = strftime("%H:%M:%S")
    current_date = strftime("%A, %d %B %Y")

    time_label.config(text=current_time)
    date_label.config(text=current_date)

    time_label.after(1000, update_time)


# Create window
root = tk.Tk()

root.title("Digital Clock")
root.geometry("600x300")
root.resizable(False, False)

# Background
root.configure(bg="#111827")


# Title
title_label = tk.Label(
    root,
    text="DIGITAL CLOCK",
    font=("Arial", 20, "bold"),
    bg="#111827",
    fg="white"
)

title_label.pack(pady=(35, 10))


# Time
time_label = tk.Label(
    root,
    text="00:00:00",
    font=("Arial", 60, "bold"),
    bg="#111827",
    fg="#00ffcc"
)

time_label.pack()


# Date
date_label = tk.Label(
    root,
    text="",
    font=("Arial", 18),
    bg="#111827",
    fg="white"
)

date_label.pack(pady=10)


# Start clock
update_time()

# Run application
root.mainloop()
