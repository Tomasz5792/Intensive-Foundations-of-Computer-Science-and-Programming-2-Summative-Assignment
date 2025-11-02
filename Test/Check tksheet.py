import tkinter as tk
import tksheet

root = tk.Tk()
sheet = tksheet.Sheet(root, data=[
    ["Name", "Age", "City"],
    ["Alice", 28, "London"],
    ["Bob", 34, "Manchester"],
])
sheet.pack(expand=True, fill="both")

root.mainloop()
