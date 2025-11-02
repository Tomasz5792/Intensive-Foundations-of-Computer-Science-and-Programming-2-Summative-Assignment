import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

# ----------------- your theming variables -----------------
colour_Green        = "#00AF41"
colour_GreenTint1   = "#49B066"
colour_GreenTint2   = "#72BD8A"
colour_GreenTint3   = "#9FCEAE"

colour_main = colour_Green
colour_menu = colour_GreenTint3

text_size = 10
text_colour =  "#000000"
text_title_colour = "#FFFFFF"
text_title_font = ("Segoe UI", 20)
text_title_padding = 10
# ----------------------------------------------------------

class App_Window(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        # Appearance and theme settings
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        self.title("Add item to table app")
        self.geometry("1200x600")
        self.minsize(900, 450)

        # Header
        self.header = Frame(self, side="top", colour_background=colour_main, height=45)
        self.header_label = ctk.CTkLabel(
            self.header,
            text="Add item to table app",
            text_color=text_title_colour,
            font=text_title_font
        )
        self.header_label.pack(side="left", padx=text_title_padding)

        # Body
        self.body = Frame(self, side="bottom")

        # Left: table
        self.table_container = Frame(self.body, side="left")
        demo_columns = ("column 1", "column 2", "column 3")
        demo_data = [
            ("1_1", "1_2", "1_3"),
            ("2_1", "2_2", "2_3"),
            ("3_1", "3_2", "3_3"),
            ("4_1", "4_2", "4_3"),
            ("5_1", "5_2", "5_3"),
            ("6_1", "6_2", "6_3"),
            ("7_1", "7_2", "7_3"),
            ("8_1", "8_2", "8_3"),
            ("9_1", "9_2", "9_3"),
            ("10_1", "10_2", "10_3"),
        ]
        self.table = Table(self.table_container, columns=demo_columns, data=demo_data)

        # Right: menu
        self.menu = Frame(self.body, side="right", colour_background=colour_menu, width=300, corner_radius=5, padding=5)

class Frame(ctk.CTkFrame):
    def __init__(
        self,
        parent,
        side: str = "left",
        colour_background: str = "transparent",
        width: int | None = None,
        height: int | None = None,
        corner_radius: int = 0,
        padding: int = 0,
    ) -> None:
        super().__init__(parent, fg_color=colour_background, corner_radius=corner_radius)

        fill = "both"
        expand = True

        if width is not None or height is not None:
            expand = False
            self.pack_propagate(False)
            if width is not None:
                fill = "y"
                self.configure(width=width)
            if height is not None:
                fill = "x"
                self.configure(height=height)

        self.pack(side=side, expand=expand, fill=fill, padx=padding, pady=padding)

class Table(ctk.CTkFrame):
    """A reusable table widget built on ttk.Treeview."""
    def __init__(self, parent, columns: tuple[str, ...], data: list[tuple] | None = None) -> None:
        super().__init__(parent)
        self.pack(fill="both", expand=True)

        # Treeview
        self.tree = ttk.Treeview(self, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=120, stretch=True)

        # Scrollbars
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.hsb = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)

        # Grid layout so the tree expands nicely
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tree.grid(row=0, column=0, sticky="nsew")
        self.vsb.grid(row=0, column=1, sticky="ns")
        self.hsb.grid(row=1, column=0, sticky="ew")

        # Insert initial data
        if data:
            for row in data:
                self.tree.insert("", "end", values=row)

    # Handy methods you can call later:
    def set_data(self, rows: list[tuple]) -> None:
        self.clear()
        for r in rows:
            self.tree.insert("", "end", values=r)

    def add_row(self, *values) -> None:
        self.tree.insert("", "end", values=values)

    def clear(self) -> None:
        for i in self.tree.get_children():
            self.tree.delete(i)

if __name__ == "__main__":
    app = App_Window()
    app.mainloop()
