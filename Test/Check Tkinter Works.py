import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Test")
root.geometry("250x150")  # Width x Height

# Add a label
label = tk.Label(root, text="Tkinter is working!", font=("Arial", 12))
label.pack(pady=20)

# Add a button to close the window
button = tk.Button(root, text="Close", command=root.destroy)
button.pack(pady=10)

# Run the app
root.mainloop()