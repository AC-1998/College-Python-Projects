###
# Course: CIS 117 Python programming
# Name: Andres Cheung
# Topics: Python GUI
# Description: For this GUI app you will create a kilometer to miles distance
#              converter.
# Date: 04/03/2023

import tkinter as tk
from tkinter import *
from tkinter import messagebox


class Convert:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x200")
        master.title("Kilometers to Miles Converter")

        self.label1 = tk.Label(master, text="Kilometers:")
        self.label1.pack()

        self.entry1 = tk.Entry(master)
        self.entry1.pack()

        self.convert_button = tk.Button(master, text="Convert",
                                        command=self.convert)
        self.convert_button.pack()

        self.quit_button = tk.Button(master, text="Quit",
                                     command=self.master.destroy)
        self.quit_button.pack()

    def convert(self):
        try:
            kilo = float(self.entry1.get())
            miles = kilo / 1.609

            messagebox.showinfo("Result", "{:.2f} miles".format(miles))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")


window = tk.Tk()
converter = Convert(window)
window.mainloop()
