import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import csv
import re
from CTkMessagebox import CTkMessagebox  



# variables

# colours
colour_Green        = "#00AF41"
colour_GreenTint1   = "#49B066"
colour_GreenTint2   = "#72BD8A"
colour_GreenTint3   = "#9FCEAE"
colour_Blue        = "#0078AF"
colour_BlueTint1   = "#399AC3"
colour_BlueTint2   = "#6DB6D2"
colour_BlueTint3   = "#A3D1E3"
colour_Grey        = "#494949"
colour_GreyTint1   = "#6D6D6D"
colour_GreyTint2   = "#939393"
colour_GreyTint3   = "#B9B9B9"


# define a non-functional accessibility requirement, such as maintaining a minimum 4.5:1 colour contrast ratio
colour_main = colour_Green
colour_menu = colour_GreenTint3
colour_button = colour_Blue

# text
text_size = 10
text_colour =  "#000000"
text_title_colour = "#FFFFFF"
text_title_font = ("Segoe UI", 20)
text__font = ("Segoe UI", 16)
text_title_padding = 10



class  AppWindow(ctk.CTk):
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
        self.header =  AppContainer(self, side = "top", colour_background = colour_main, height = 45)
        
        self.header_label = ctk.CTkLabel(self.header, 
                                        text="Add item to table app",
                                        text_color=text_title_colour,
                                        font=(text_title_font)
                                        )
        self.header_label.pack(side="left", padx=text_title_padding)

        self.body =  AppContainer(self, side = "bottom")

        self.table_container =  AppContainer(self.body, side = "left", padding_verticle = 5, padding_horizontal = 5)
        self.table =  AppTable(self.table_container)

        self.menu =  AppContainer(self.body, side = "right", colour_background = colour_menu, width = 300, corner_radius = 5, padding_verticle = 5, padding_horizontal = (0,5))
        self.text_input_FirstName = InputName(self.menu, placeholder_text="First Name")
        self.text_input_MiddleName = InputName(self.menu, placeholder_text="Middle Name")
        self.text_input_LastName = InputName(self.menu, placeholder_text="Last Name")
        self.text_input_TelephoneNo = InputTelephoneNo(self.menu, placeholder_text="Telephone No")
        
        self.add_item_button =  AppButton(self.menu, text="Clear Inputs", command=self.clear_input)
        self.add_item_button =  AppButton(self.menu, text="Add New Item", command=self.on_add_item)

    def on_add_item(self):
        # Retrieve input values
        first_name = self.text_input_FirstName.get_value()
        middle_name = self.text_input_MiddleName.get_value()
        last_name = self.text_input_LastName.get_value()
        telephone_no = self.text_input_TelephoneNo.get_value()

        # Validate input values
        bool_TelephoneNo_Validation = self.text_input_TelephoneNo.validate_telephone_no(telephone_no)

        if first_name == "" or middle_name == "" or last_name == "" or telephone_no == "":
            self.show_messagebox(
                title="Please fill in all fields",
                message="All fields are required. Please complete all input fields before submitting.",
                icon="info"
            )
        
        if bool_TelephoneNo_Validation or bool_TelephoneNo_Validation:  # add other validations here
            self.show_messagebox(
                title="title",
                message="message",
                icon="warning"
            )
        
        # Add logic to insert the new item into the table or data source

    def clear_input(self):
        self.text_input_FirstName.clear_input()
        self.text_input_MiddleName.clear_input()
        self.text_input_LastName.clear_input()
        self.text_input_TelephoneNo.clear_input()

    def show_messagebox(self, title: str, message: str, icon: str = "info"):
        """
        Displays a message box with the specified title, message, and icon.

        Args:
            title (str): The title of the message box.
            message (str): The message to display in the message box.
            icon (str, optional): The icon type for the message box. Defaults to "info".

        Returns:
            None
        """
        CTkMessagebox(
            title=title,
            message=message,
            icon=icon
        ).show()


class  AppContainer(ctk.CTkFrame):
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
        # if width is not None or height is not None:
        #     expand = False
        #     self.pack_propagate(False)
        #     if width is not None:
        #         fill = "y"
        #         self.configure(width=width)
        #     if height is not None:
        #         fill = "x"
        #         self.configure(height=height)
        
        if width is not None or height is not None:
            expand = False
            self.pack_propagate(False)

            if width is not None:
                self.configure(width=width)
                fill = "y"
            if height is not None:
                self.configure(height=height)
                fill = "x"
        else:
            fill = "both"
            expand = True


        self.pack(side=side, expand = expand, fill = fill, padx=padding_horizontal, pady=padding_verticle)


class  AppTable(ctk.CTkFrame):
    def __init__(
            self, 
            parent,
            ) -> None:
        super().__init__(parent, 
                         #fg_color="transparent", corner_radius=10, border_width=0 ## trying to make the border dissapear
                         )
        
        style = ttk.Style(self)

        style.layout(
            "NoBorder.Treeview",
            [("Treeview.treearea", {"sticky": "nswe"})]
        )
        style.configure("NoBorder.Treeview.Heading", font=("Segoe UI", 14), borderwidth=0, relief="flat")
        style.configure("NoBorder.Treeview", font=("Segoe UI", 13), rowheight=28)

        self.pack(fill="both", expand=True)
        self.tree = ttk.Treeview(self, columns=(), show="headings", 
                                 style="NoBorder.Treeview"
                                 )

        # Scrollbars
        self.verticle_Scroll = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.horizontal_Scroll = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        self.tree.configure(
            yscrollcommand=self.verticle_Scroll.set, 
            xscrollcommand=self.horizontal_Scroll.set
            )

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
    

class AppButton(ctk.CTkButton):
    """
    A reusable customtkinter button with consistent styling.
        
    Args:
        parent (CTk or CTkFrame): The parent widget this will be placed inside.
        text ( str ): The text to display on the button.
        command ( function, optional ): The function to call when the button is clicked. Defaults to None.
        
    Methods:
        None

    Returns:
            None
    """
    def __init__(
            self, 
            parent,
            text: str,
            command = None,
            ) -> None:
        """
        Initializes the AppButton with consistent styling.
        
        Args:
            parent (CTk or CTkFrame): The parent widget this will be placed inside.
            text ( str ): The text to display on the button.
            command ( function, optional ): The function to call when the button is clicked. Defaults to None.
        """
        super().__init__(
            parent, 
            text=text, 
            command=command,
            font=text__font,
            fg_color=colour_button,
            hover_color=colour_BlueTint1,
            text_color=text_title_colour,
            corner_radius=5,
            #fg_color_disabled=colour_GreyTint1, #doesn't apear to be a real input
            )
        
        side = "top"
        fill = "x"
        expand = False
        padding_verticle = (5,5)
        padding_horizontal = (5,5)
        
        self.pack(side=side, expand = expand, fill = fill, padx=padding_horizontal, pady=padding_verticle)


class InputText(ctk.CTkEntry):
    """
    A reusable customtkinter text input with consistent styling.
        
    Args:
        parent (CTk or CTkFrame): The parent widget this will be placed inside.
        placeholder_text ( str ): The text to display in this input.
        
    Methods:
        def get_value(self) -> str:  retrieves the current text value from the input field.
        def clear_input(self):  clears the text in the input field.
        
    Returns:
            None
    """
    def __init__(
            self, 
            parent,
            placeholder_text: str = "",
            ) -> None:
        super().__init__(
            parent,
            placeholder_text=placeholder_text,
            font=text__font,
            corner_radius=5,
            border_width=1,
            border_color=colour_GreyTint2,
            )
        
        side = "top"
        fill = "x"
        expand = False
        padding_verticle = (5,5)
        padding_horizontal = (5,5)
        
        self.pack(side=side, expand = expand, fill = fill, padx=padding_horizontal, pady=padding_verticle)

    def get_value(self) -> str:
        """
        Retrieves the current text value from the input field.

        Returns:
            str: The current text value in the input field.
        """
        print(self._name,": ", self.get())
        return self.get()
    
    def clear_input(self):
        self.delete(0, "end")
    

class InputName(InputText):
    """
    A reusable customtkinter name input with consistent styling.
        
    Args:
        parent (CTk or CTkFrame): The parent widget this will be placed inside.
        placeholder_text ( str ): The text to display in this input.
        
    Methods:
        None

    Returns:
            None
    """
    def __init__(
            self, 
            parent,
            placeholder_text: str = "",
            ) -> None:
        super().__init__(
            parent,
            placeholder_text=placeholder_text,
            )
        

class InputTelephoneNo(InputText):
    """
    A reusable customtkinter telephone number input with consistent styling.
        
    Args:
        parent (CTk or CTkFrame): The parent widget this will be placed inside.
        placeholder_text ( str ): The text to display in this input.
        
    Methods:
        None

    Returns:
            None
    """
    def __init__(
            self, 
            parent,
            placeholder_text: str = "",
            ) -> None:
        super().__init__(
            parent,
            placeholder_text=placeholder_text,
            )

    def validate_telephone_no(self, telephone_no: str) -> bool:
        """
        Validates the telephone number format.

        Args:
            telephone_no (str): The telephone number to validate.

        Returns:
            bool: True if the telephone number is valid, False otherwise.
        """
        cleaned = telephone_no.replace(" ", "")

        mobile_pattern = r"^07\d{9}$"  # UK mobile format eg 07123456789
        landline_pattern = r"^0(1|2)\d{8,9}$"  # UK landline format eg 01234567890 or 02012345678
        intl_pattern = r"^\+447\d{9}$"  # UK international format eg +447912345678

        passed_Validation = bool(
            re.match(mobile_pattern, cleaned) or 
            re.match(landline_pattern, cleaned) or 
            re.match(intl_pattern, cleaned)
        )

        print(self._name,": ", passed_Validation)

        return passed_Validation

if __name__ == "__main__":
    app =  AppWindow()
    app.mainloop()
    
