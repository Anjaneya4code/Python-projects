import tkinter as tk
from tkinter import messagebox
import qrcode


def generate_qr():
    data = entry.get().strip()

    if not data:
        messagebox.showwarning(
            "Warning",
            "Please enter text or a URL."
        )
        return

    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    # Generate image
    image = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    # Save image
    image.save("generated_qr.png")

    messagebox.showinfo(
        "Success",
        "QR Code generated successfully!\n\n"
        "Saved as generated_qr.png"
    )


# Main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg="#111827")


# Title
title = tk.Label(
    root,
    text="QR CODE GENERATOR",
    font=("Arial", 24, "bold"),
    bg="#111827",
    fg="white"
)

title.pack(pady=35)


# Instruction
label = tk.Label(
    root,
    text="Enter text or URL:",
    font=("Arial", 14),
    bg="#111827",
    fg="white"
)

label.pack()


# Input field
entry = tk.Entry(
    root,
    width=45,
    font=("Arial", 14)
)

entry.pack(pady=15)


# Generate button
button = tk.Button(
    root,
    text="Generate QR Code",
    font=("Arial", 13, "bold"),
    bg="#00c896",
    fg="white",
    padx=20,
    pady=10,
    command=generate_qr
)

button.pack()


# Run application
root.mainloop()
