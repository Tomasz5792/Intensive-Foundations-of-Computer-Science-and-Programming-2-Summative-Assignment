import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import csv


# variables

# colours
colour_Green        = "#00AF41"
colour_GreenTint1   = "#49B066"
colour_GreenTint2   = "#72BD8A"
colour_GreenTint3   = "#9FCEAE"

colour_main = colour_Green
colour_menu = colour_GreenTint3

# text
text_size = 10
text_colour =  "#000000"
text_title_colour = "#FFFFFF"
text_title_font = ("Segoe UI", 20)
text__font = ("Segoe UI", 16)
text_title_padding = 10

def setup_styles():
    
    style = ttk.Style()
    style.theme_use("default")

    # table body style
    style.configure("Treeview",
        background="#2a2d2e",
        foreground="white",
        rowheight=25,
        fieldbackground="#343638",
        bordercolor="#343638",
        borderwidth=0,
        font=text__font,
        )

    # selected row
    style.map("Treeview",
    background=[('selected', '#22559b')])

    # header style
    style.configure("Treeview.Heading",
        background="#565b5e",
        foreground="white",
        relief="flat",
        font=text_title_font,
        )

    style.map("Treeview.Heading",
    background=[('active', '#3484F0')])


class App_Window(ctk.CTk):
    #main window class
    def __init__(self) -> None:
        """
        Initialises the app window and configures its settings.

        Returns:
            None
        """
        super().__init__()

        # Appearance and theme settings
        ctk.set_appearance_mode("light")  # "light" or "dark"  add a mode toggle
        ctk.set_default_color_theme("green")  # make defra green

        # settings
        self.title("Add item to table app")
        self.geometry("1200x600")
        self.minsize(900, 450)

        # components
        self.header = Frame(self, side = "top", colour_background = colour_main, height = 45)
        
        self.header_label = ctk.CTkLabel(self.header, 
                                        text="Add item to table app",
                                        text_color=text_title_colour,
                                        font=(text_title_font)
                                        )
        self.header_label.pack(side="left", padx=text_title_padding)

        self.body = Frame(self, side = "bottom")

        self.table_container = Frame(self.body, side = "left", padding_verticle = 5, padding_horizontal = 5)
        self.table = Table(self.table_container)

        self.menu = Frame(self.body, side = "right", colour_background = colour_menu, width = 300, corner_radius = 5, padding_verticle = 5, padding_horizontal = (0,5))


class Frame(ctk.CTkFrame):
    def __init__(
            self, 
            parent, 
            side: str = "left", 
            colour_background: str = "transparent",
            width: int | None = None,
            height: int | None = None,
            #fill: str = "both",
            #expand: bool = True,
            corner_radius: int = 0,
            padding_verticle: tuple[int, int] = (0,0),
            padding_horizontal: tuple[int, int] = (0,0),
            ) -> None:
        """
        A reusable customtkinter frame with flaxible layout and colour options.

        Args:
            parent (CTk or CTkFrame): The parent widget this frame will be placed inside.
            side (str, optional): The side of the parent to pack the frame on. Defaults to "left".
            colour_background (str, optional): The background color of the frame. Defaults to "transparent".
            width (int | None, optional): Fixed width of the frame in pixels. If set, the frame will not expand horizontally. Defaults to None.
            height (int | None, optional): Fixed height of the frame in pixels. If set, the frame will not expand vertically. Defaults to None.
            corner_radius (int, optional): Corner roundness of the frame in pixels. Defaults to 0.
            padding (int, optional): External padding (in pixels) applied equally on all sides. Defaults to 0.

        Returns:
            None
        """

        super().__init__(parent, fg_color=colour_background, corner_radius=corner_radius)

        fill = "both"
        expand = True

        # fixed size
        if width is not None or height is not None:
            expand = False
            self.pack_propagate(False)
            if width is not None:
                fill = "y"
                self.configure(width=width)
            if height is not None:
                fill = "x"
                self.configure(height=height)

        self.pack(side=side, expand = expand, fill = fill, padx=padding_horizontal, pady=padding_verticle)


class Table(ctk.CTkFrame):
    def __init__(
            self, 
            parent,
            ) -> None:
        super().__init__(parent)



        self.pack(fill="both", expand=True)
        self.tree = ttk.Treeview(self, columns=(), show="headings", style="Custom.Treeview")

        # Scrollbars
        self.verticle_Scroll = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.horizontal_Scroll = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.verticle_Scroll.set, xscrollcommand=self.horizontal_Scroll.set)

        # Layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.verticle_Scroll.grid(row=0, column=1, sticky="ns")
        self.horizontal_Scroll.grid(row=1, column=0, sticky="ew")

        self.load_csv_file()


    def load_csv_file(self):
        with open("table_data.csv", newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)

        columns = rows[0]
        data = rows[1:]

        self.tree["columns"] = columns

        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, anchor="center", stretch=True)

        # clear existing
        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in data:
            self.tree.insert("", "end", values=row)
    

if __name__ == "__main__":
    app = App_Window()
    setup_styles()
    app.mainloop()
    
