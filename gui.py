import tkinter as tk
from tkinter import messagebox


def generate_qr():
    website = url_entry.get
    filename = filename_entry.get()
    if website and filename:
        pass
    else:
        messagebox.showerror("Error", "Please enter both website URL and filename.")

window = tk.Tk()
window.title("QR Code Generator")

tk.Label(window, text = "Website:").pack()
url_entry = tk.Entry(window)
url_entry.pack(padx = 20)

tk.Label(window, text = "File name of  QR Code:").pack()
filename_entry = tk.Entry(window)
filename_entry.pack(padx = 20)

generate_button = tk.Button(window, text =  "Generate QR Code", command = generate_qr)
generate_button.pack()

window.mainloop()

