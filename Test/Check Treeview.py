import tkinter as tk
from tkinter import ttk

class TableApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Table Example")
        self.geometry("400x250")

        # Create the table
        self.create_table()

    def create_table(self):
        # Define columns
        columns = ("ID", "Name", "Age")

        # Create Treeview
        self.tree = ttk.Treeview(self, columns=columns, show="headings")

        # Define headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        # Insert sample data
        data = [
            (1, "Alice", 28),
            (2, "Bob", 34),
            (3, "Charlie", 25),
        ]
        for row in data:
            self.tree.insert("", "end", values=row)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        # Layout
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

# Run the app
if __name__ == "__main__":
    app = TableApp()
    app.mainloop()
