import tkinter as tk
from tkinter import ttk, messagebox

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        
        # Input field
        tk.Label(root, text="Enter value:").grid(row=0, column=0)
        self.value_entry = tk.Entry(root)
        self.value_entry.grid(row=0, column=1)
        
        # Conversion options
        tk.Label(root, text="Convert from:").grid(row=1, column=0)
        self.from_unit = ttk.Combobox(root, values=["Meters", "Celsius"]) # thêm "Celsius" vào danh sách đơn vị đo
        self.from_unit.grid(row=1, column=1)
        self.from_unit.current(0) # chọn "Meters" làm giá trị mặc định
        
        tk.Label(root, text="Convert to:").grid(row=2, column=0)
        self.to_unit = ttk.Combobox(root, values=["Feet", "Fahrenheit"]) # thêm "Fahrenheit" vào danh sách đơn vị đo
        self.to_unit.grid(row=2, column=1)
        self.to_unit.current(0) # chọn "Feet" làm giá trị mặc định
        
        # Result field
        tk.Label(root, text="Result:").grid(row=3, column=0)
        self.result_entry = tk.Entry(root, state='readonly')
        self.result_entry.grid(row=3, column=1)
        
        # Convert button
        tk.Button(root, text="Convert", command=self.convert).grid(row=4, column=0, columnspan=2)
    
    def convert(self):
        try:
            value = float(self.value_entry.get())
            from_unit = self.from_unit.get()
            to_unit = self.to_unit.get()
            
            if from_unit == "Meters" and to_unit == "Feet":
                result = value * 3.28084
            elif from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = (value * 9/5) + 32
            else:
                messagebox.showerror("Conversion Error", "Invalid conversion selected.")
                return
            
            self.result_entry.config(state='normal')
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, str(result))
            self.result_entry.config(state='readonly')
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()