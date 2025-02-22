import tkinter as tk
from tkinter import ttk

class BgColors:
    def __init__(self, root):
        self.root = root
        root.geometry("300x100")
        self.root.title("Background Colors")

        # Background color selection
        tk.Label(self.root, text="Background Color:").grid(row=0, column=0)
        self.color_choices = ["White", "Light Blue", "Light Green", "Yellow", "Pink"]
        self.color_dropdown = ttk.Combobox(self.root, values=self.color_choices, state="readonly")
        self.color_dropdown.grid(row=0, column=1)
        self.color_dropdown.current(0)
        self.color_dropdown.bind("<<ComboboxSelected>>", self.change_background)
        
        # Change button
        tk.Button(root, text="Change", command=self.change_background).grid(row=1, column=0, columnspan=2)

    def change_background(self, event=None):
        selected_color = self.color_dropdown.get()
        color_mapping = {
            "White": "white",
            "Light Blue": "light blue",
            "Light Green": "light green",
            "Yellow": "yellow",
            "Pink": "pink"
        }
        self.root.configure(bg=color_mapping[selected_color])

if __name__ == "__main__":
    root = tk.Tk()
    app = BgColors(root)
    root.mainloop()
