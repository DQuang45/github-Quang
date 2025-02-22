import tkinter as tk
import random

class RandomNumberGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Number Generator")

        # Min input
        tk.Label(self.root, text="Min:").grid(row=0, column=0)
        self.min_entry = tk.Entry(self.root)
        self.min_entry.grid(row=0, column=1)

        # Max input
        tk.Label(self.root, text="Max:").grid(row=1, column=0)
        self.max_entry = tk.Entry(self.root)
        self.max_entry.grid(row=1, column=1)

        # Generate button
        tk.Button(self.root, text="Generate", command=self.generate_number).grid(row=2, column=0, columnspan=2)

        # Result label (Hiển thị số ngẫu nhiên)
        self.result_label = tk.Label(self.root, text="Random Number: ", font=("Arial", 12))
        self.result_label.grid(row=3, column=0, columnspan=2)

        # Show Quote button
        tk.Button(self.root, text="Show Quote", command=self.show_quote).grid(row=4, column=0, columnspan=2)

        # Quote Label
        self.quote_label = tk.Label(self.root, text="", wraplength=300, font=("Arial", 10, "italic"))
        self.quote_label.grid(row=5, column=0, columnspan=2)

        # List of quotes
        self.quotes = [
            "Believe you can and you're halfway there.",
            "Keep going. Everything you need will come to you at the perfect time.",
            "The only limit to our realization of tomorrow is our doubts of today.",
            "Don't watch the clock; do what it does. Keep going.",
            "Act as if what you do makes a difference. It does."
        ]

    def generate_number(self):
        try:
            # Lấy giá trị min và max từ input
            min_val = int(self.min_entry.get())
            max_val = int(self.max_entry.get())

            if min_val >= max_val:
                raise ValueError("Min must be less than Max!")

            # Tạo số ngẫu nhiên
            random_num = random.randint(min_val, max_val)
            self.result_label.config(text=f"Random Number: {random_num}", fg="black")

        except ValueError as e:
            self.result_label.config(text=f"Error: {str(e)}", fg="red")

    def show_quote(self):
        self.quote_label.config(text=random.choice(self.quotes))

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomNumberGenerator(root)
    root.mainloop()
