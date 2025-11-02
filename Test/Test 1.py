import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

class App_Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Nested Frames Example")
        self.geometry("800x500")

        # Main container frame (fills window)
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Top and bottom frames inside main_frame
        top_frame = ctk.CTkFrame(main_frame, fg_color="lightgreen")
        top_frame.pack(side="top", fill="x", padx=5, pady=5)

        bottom_frame = ctk.CTkFrame(main_frame, fg_color="white")
        bottom_frame.pack(side="bottom", expand=True, fill="both", padx=5, pady=5)

        # Frames *inside* the bottom frame (side by side)
        left_sub = ctk.CTkFrame(bottom_frame, fg_color="green")
        left_sub.pack(side="left", expand=True, fill="both", padx=5, pady=5)

        right_sub = ctk.CTkFrame(bottom_frame, fg_color="lightgrey")
        right_sub.pack(side="right", expand=True, fill="both", padx=5, pady=5)

        # Add some labels to visualize layout
        ctk.CTkLabel(top_frame, text="Top Frame").pack()
        ctk.CTkLabel(left_sub, text="Left Frame").pack()
        ctk.CTkLabel(right_sub, text="Right Frame").pack()

app = App_Window()
app.mainloop()
