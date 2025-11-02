import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

class App_Window(ctk.CTk):
    """Main window layout with header, red content area, and purple sidebar."""
    def __init__(self) -> None:
        super().__init__()

        # Window setup
        self.title("Title")
        self.geometry("1200x600")
        self.minsize(900, 450)

        # Header (fixed height)
        self.header = Frame(self, side="top", colour_background="blue",
                            expand=False, fill="x", height=50)

        # Body (takes the rest)
        self.body = Frame(self, side="top", colour_background="transparent",
                          expand=True, fill="both")

        # Inside body: red (main) and purple (sidebar)
        self.table = Frame(self.body, side="left", colour_background="red",
                           expand=True, fill="both")
        self.menu = Frame(self.body, side="left", colour_background="purple",
                           expand=True, fill="both")

class Frame(ctk.CTkFrame):
    """A reusable frame with color, optional fixed size, and pack settings."""
    def __init__(
        self,
        parent,
        side: str = "left",
        colour_background: str = "transparent",
        *,
        expand: bool = True,
        fill: str = "both",
        width: int | None = None,
        height: int | None = None,
    ) -> None:
        super().__init__(parent, fg_color=colour_background)  # ✅ use fg_color directly

        # Optional fixed size
        if width is not None or height is not None:
            self.pack_propagate(False)
            if width is not None:
                self.configure(width=width)
            if height is not None:
                self.configure(height=height)

        # Pack frame into parent
        self.pack(side=side, expand=expand, fill=fill)

app = App_Window()
app.mainloop()
