import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import csv
import re
from CTkMessagebox import CTkMessagebox
import tkinter.messagebox as messagebox
from datetime import datetime



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
colour_Grey        = "#383838"
colour_GreyTint1   = "#6D6D6D"
colour_GreyTint2   = "#939393"
colour_GreyTint3   = "#B9B9B9"


# define a non-functional accessibility requirement, such as maintaining a minimum 4.5:1 colour contrast ratio
colour_main = colour_Green
colour_menu = colour_GreenTint3
colour_button = colour_Blue

# text
text_size = 10
text_colour =  colour_Grey
text_title_colour = "#FFFFFF"
text_title_font = ("Segoe UI", 20)
text__font = ("Segoe UI", 16)
text_title_padding = 10

directorates = [
    "",
    "Agri Food Chain Directorate",
    "Environment Quality Directorate",
    "Animal and Plant Health Directorate",
    "Digital Data and Technology Services Directorate",
    "Water and Flood Management Directorate",
    "Science Capability in Animal Health Directorate",
    "Analysis Directorate",
    "Transformation Directorate",
    "Environment and Rural Group",
    "Food and Farming Group"
]


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
        self.minsize(900, 500)

        # components
        self.header =  AppContainer(self, side = "top", colour_background = colour_main, height = 45)
        
        self.header_label = ctk.CTkLabel(self.header, 
                                        text="Add item to table app",
                                        text_color=text_title_colour,
                                        font=(text_title_font)
                                        )
        self.header_label.pack(side="left", padx=text_title_padding)

        self.body =  AppContainer(self, side = "bottom")

        self.menu =  AppContainer(self.body, side = "right", colour_background = colour_menu, width = 300, corner_radius = 5, padding_verticle = 5, padding_horizontal = (0,5))
        
        self.table_container =  AppContainer(self.body, side = "left", padding_verticle = 5, padding_horizontal = 5)
        self.table =  AppTable(self.table_container)

        self.Label_FirstName = AppLabel(self.menu, text="First Name:")
        self.text_input_FirstName = InputName(self.menu, placeholder_text="eg. John")

        self.Label_MiddleName = AppLabel(self.menu, text="Middle Name:")
        self.text_input_MiddleName = InputName(self.menu, placeholder_text="eg. Michael")

        self.Label_LastName = AppLabel(self.menu, text="Last Name:")
        self.text_input_LastName = InputName(self.menu, placeholder_text="eg. Smith")

        self.Label_TelephoneNo = AppLabel(self.menu, text="Telephone No:")
        self.text_input_TelephoneNo = InputTelephoneNo(self.menu, placeholder_text="eg. 07123456789 or 01234567890")
        
        self.Label_Directorate = AppLabel(self.menu, text="Directorate:")
        self.dropdown_Directorate = InputDropdown(self.menu, options=directorates)

        self.add_item_button =  AppButton(self.menu, text="Add New Item", command=self.on_add_item)
        self.add_item_button =  AppButton(self.menu, text="Clear Inputs", command=self.clear_input)
        

    def on_add_item(self):
        """
        Handles the logic for adding a new item to the table when the "Add New Item" button is clicked.
        Args:
            None
        Returns:
            None
        """
        # Retrieve input values
        first_name = self.text_input_FirstName.get_value()
        middle_name = self.text_input_MiddleName.get_value()
        last_name = self.text_input_LastName.get_value()
        telephone_no = self.text_input_TelephoneNo.get_value()
        directorate = self.dropdown_Directorate.get_value()

        # Validate input values
        bool_FirstName_Validation, str_FirstName_Error = self.text_input_FirstName.validate_name(first_name, "First name")
        bool_MiddleName_Validation, str_MiddleName_Error = self.text_input_MiddleName.validate_name(middle_name, "Middle name")
        bool_LastName_Validation, str_LastName_Error = self.text_input_LastName.validate_name(last_name, "Last name")
        bool_TelephoneNo_Validation, str_TelephoneNo_Error = self.text_input_TelephoneNo.validate_telephone_no(telephone_no)

        if first_name == "" or middle_name == "" or last_name == "" or telephone_no == "" or directorate == "":
            self.show_messagebox(
                title="Please fill in all fields",
                message="All fields are required. Please complete all input fields before submitting.",
                icon="info"
            )

        elif not bool_FirstName_Validation:
            self.show_messagebox(
                title="First Name Validation Error",
                message=str_FirstName_Error,
                icon="warning"
            )

        elif not bool_MiddleName_Validation:
            self.show_messagebox(
                title="Middle Name Validation Error",
                message=str_MiddleName_Error,
                icon="warning"
            )

        elif not bool_LastName_Validation:
            self.show_messagebox(
                title="Last Name Validation Error",
                message=str_LastName_Error,
                icon="warning"
            )
        
        elif not bool_TelephoneNo_Validation:
            self.show_messagebox(
                title="Telephone Number Validation",
                message=str_TelephoneNo_Error,
                icon="warning"
            )

        else:
            self.show_messagebox(
                title="Item Added Successfully",
                message=f"New item added:\nFirst Name: {first_name}\nMiddle Name: {middle_name}\nLast Name: {last_name}\nTelephone No: {telephone_no}\nDirectorate: {directorate}",
                icon="info"
            )
           
            self.append_to_csv(first_name, middle_name, last_name, telephone_no, directorate)  #append to csv file
            self.table.load_csv_file()  #reload table data
            self.clear_input()  #clear inputs

    def append_to_csv(self, first_name, middle_name, last_name, telephone_no, directorate):
        """
        Appends a new record to the table_data.csv file.

        Args:
            first_name (str): First name
            middle_name (str): Middle name
            last_name (str): Last name
            telephone_no (str): Telephone number
            directorate (str): Directorate

        Returns:
            None
        """

        file_path = "table_data.csv"
        time_and_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(file_path, "a", newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([first_name, middle_name, last_name, telephone_no, directorate, time_and_date])
            print(f"Record added: {first_name}, {middle_name}, {last_name}, {telephone_no}, {directorate}, {time_and_date}")
        except Exception as e:
            self.show_messagebox("Error", f"Failed to write to CSV: {e}", icon="error")

    def clear_input(self):
        self.text_input_FirstName.clear_input()
        self.text_input_MiddleName.clear_input()
        self.text_input_LastName.clear_input()
        self.text_input_TelephoneNo.clear_input()
        self.dropdown_Directorate.clear_input()
        self.table.load_csv_file()  #reload table data

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
        # CTkMessagebox(
        #     title=title,
        #     message=message,
        #     icon=icon
        # ).show()

        if icon == "warning":
            messagebox.showwarning(title, message)
        elif icon == "error":
            messagebox.showerror(title, message)
        else:
            messagebox.showinfo(title, message)


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
        columns = [c for c in columns if c != "Date Time Added"]
        data = rows[1:]

        self.tree["columns"] = columns
        
        width_table = self.tree.winfo_width() #I would like this to change when the screen size changes not just on loading the data
        print("Table width: ", width_table)
        if width_table <= 1:
            width_table = 1300-10  # default width if not yet rendered
        column_width = (width_table -10) // len(columns)

        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, anchor="center", stretch=False, width=column_width) #trying to get the horizontal scroll bar used

        # clear existing
        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in data:
            altered_row = [
                value
                for i, value in enumerate(row)
                if i < len(columns) and columns[i] != "Date Time Added"
            ]
            self.tree.insert("", "end", values=altered_row)
    

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
            side: str = "bottom",
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
        
        #side = "top"
        fill = "x"
        expand = False
        padding_verticle = (0,10)
        padding_horizontal = (5,5)
        
        self.pack(side=side, expand = expand, fill = fill, padx=padding_horizontal, pady=padding_verticle)


class AppLabel(ctk.CTkLabel):
    """
    A reusable customtkinter label with consistent styling.
        
    Args:
        parent (CTk or CTkFrame): The parent widget this will be placed inside.
        text ( str ): The text to display on the label.
        
    Methods:
        None

    Returns:
            None
    """
    def __init__(
            self, 
            parent,
            text: str,
            ) -> None:
        super().__init__(
            parent,
            text=text,
            font=text__font,
            text_color=text_colour,
            #justify="left",
            anchor="w",
            #bg_color="red"  #for testing aligment
            )
        
        side = "top"
        fill = "x"
        expand = False
        padding_verticle = (5,0)
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
        padding_verticle = (5,0)
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
        validate_name(self, name: str, TextInput_Name: str) -> tuple[bool, str]:  Validates the name format.

    Returns:
            None
    """
    def __init__(
            self, 
            parent,
            placeholder_text: str = "",
            #TextInput_Name: str = "Error",
            ) -> None:
        super().__init__(
            parent,
            placeholder_text=placeholder_text,
            )
    
    def validate_name(self, name: str, TextInput_Name: str) -> tuple[bool, str]:
        """
        Validates the name format.

        Args:
            placeholder_text (str): The string to validate.
            TextInput_Name (str): The name of the text input field.

        Returns:
            tuple[bool, str]: True if the name is valid, False otherwise.  Also returns an error message.

        Validation logic:
            Must not be empty.
            Must contain only letters (a-z, A-Z), spaces, hyphens (-), or apostrophes (').
            Must not contain multiple spaces or hyphens in a row.
            Each part of the name (separated by spaces, hyphens, or apostrophes) must start with a capital letter.
        """
        Error_Message = "None"
        cleaned = name.strip()

        if cleaned == "":
            Error_Message = TextInput_Name + " can not be empty."
            print(self._name,": ", False, "Message: ", Error_Message)
            return False, Error_Message

        if re.search(r"[^a-zA-Z '-]", name):
            Error_Message = TextInput_Name + " must contain only letters, spaces, hyphens, or apostrophes."
            print(self._name, ": ", False, "Message:", Error_Message)
            return False, Error_Message
        
        if re.search(r"[ -]{2,}| -|- ", name):  # checks for multiple spaces or hyphens in a row
            Error_Message = TextInput_Name + " cannot contain multiple spaces or hyphens in a row."
            print(self._name, ":", False, "Message:", Error_Message)
            return False, Error_Message
        
        def check_if_capitalised(word: str) -> bool:
            for part in word.split(" "):
                for subpart in part.split("-"):
                    for subpart2 in subpart.split("'"):
                        if not subpart2 or subpart2 != subpart2.capitalize():
                            return False
            return True
        
        if not check_if_capitalised(name):
            Error_Message = TextInput_Name + " must be capitalised (e.g., John, O'Connor, Anne-Marie)."
            print(self._name, ":", False, "Message:", Error_Message)
            return False, Error_Message

        passed_Validation = True
        Error_Message = TextInput_Name + " is valid."

        print(self._name,": ", passed_Validation, "Message: ", Error_Message)

        return passed_Validation, Error_Message
        

class InputTelephoneNo(InputText):
    """
    A reusable customtkinter telephone number input with consistent styling.
        
    Args:
        parent (CTk or CTkFrame): The parent widget this will be placed inside.
        placeholder_text ( str ): The text to display in this input.
        
    Methods:
        validate_telephone_no(self, telephone_no: str) -> tuple[bool, str]:  Validates the telephone number format.

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

    def validate_telephone_no(self, telephone_no: str) -> tuple[bool, str]:
        """
        Validates the telephone number format.

        Args:
            telephone_no (str): The telephone number to validate.

        Returns:
            tuple[bool, str]: True if the telephone number is valid, False otherwise.  Also returns an error message.

        Validation logic:
            Must not be empty.
            Must contain only numbers (0-9) and an optional leading '+' for international format.
            The '+' sign can only appear at the beginning of the number.
            Must match one of the following UK telephone number formats:
                - UK mobile format: 07XXXXXXXXX (11 digits starting with '07')
                - UK landline format: 0XYYYYYYYYY or 0XXYYYYYYYY (10 or 11 digits starting with '01' or '02')
                - UK international format: +447XXXXXXXXX (13 digits starting with '+447')
        """
        Error_Message = "Error"
        cleaned = telephone_no.replace(" ", "")

        if cleaned == "":
            Error_Message = "Telephone number can not be empty."
            print(self._name,": ", False, "Message: ", Error_Message)
            return False, Error_Message

        if re.search(r"[^0-9+]", telephone_no):
            Error_Message = "Telephone number must contain only numbers no letters or symbols."
            print(self._name, ": ", False, "Message:", Error_Message)
            return False, Error_Message

        if "+" in telephone_no[1:]:
            Error_Message = "The '+' sign can only appear at the beginning of the number."
            print(self._name, ": ", False, "Message:", Error_Message)
            return False, Error_Message
 
        mobile_pattern = r"^07\d{9}$"  # UK mobile format eg 07123456789
        landline_pattern = r"^0(1|2)\d{8,9}$"  # UK landline format eg 01234567890 or 02012345678
        intl_pattern = r"^\+447\d{9}$"  # UK international format eg +447912345678

        passed_Validation = bool(
            re.match(mobile_pattern, telephone_no) or 
            re.match(landline_pattern, telephone_no) or 
            re.match(intl_pattern, telephone_no)
        )
        if passed_Validation:
            Error_Message = "Telephone number is valid."
        else:
            Error_Message = "Invalid telephone number format. Please enter a valid UK telephone number. Examples: 07123456789, 01234567890, +447912345678."

        print(self._name,": ", passed_Validation, "Message: ", Error_Message)

        return passed_Validation, Error_Message


class InputDropdown(ctk.CTkOptionMenu):
    def __init__(
            self, 
            parent,
            options: list[str],
            ) -> None:
        super().__init__(
            parent,
            values=options,
            font=text__font,
            corner_radius=5,
            fg_color="white",
            button_color="white",
            button_hover_color=colour_BlueTint3,
            text_color="black",
            dropdown_fg_color="white",
            dropdown_text_color="black",
            dropdown_hover_color=colour_BlueTint3,
            bg_color="transparent",
            )
        
        
        side = "top"
        fill = "x"
        expand = False
        padding_verticle = (5,0)
        padding_horizontal = (5,5)
        
        self.pack(side=side, expand = expand, fill = fill, padx=padding_horizontal, pady=padding_verticle)

    def get_value(self) -> str:
        """
        Retrieves the currently selected value from the dropdown.

        Returns:
            str: The currently selected value in the dropdown.
        """
        print(self._name,": ", self.get())
        return self.get()
    
    def clear_input(self):
        self.set("")
    

if __name__ == "__main__":
    app =  AppWindow()
    app.mainloop()
    
