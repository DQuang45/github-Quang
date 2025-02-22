import tkinter as tk
from tkinter import messagebox # hiển thị thông báo pop-up khi người dùng nhấn "Submit"

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")
        
        # Input fields
        tk.Label(root, text="Enter first number:").grid(row=0, column=0)
        self.num1_entry = tk.Entry(root)
        self.num1_entry.grid(row=0, column=1)
        
        tk.Label(root, text="Enter second number:").grid(row=1, column=0)
        self.num2_entry = tk.Entry(root)
        self.num2_entry.grid(row=1, column=1)
        
        # Result field
        tk.Label(root, text="Result:").grid(row=2, column=0)
        self.result_entry = tk.Entry(root, state='readonly')
        self.result_entry.grid(row=2, column=1)
        
        # Buttons
        tk.Button(root, text="+", command=self.add).grid(row=0, column=2, padx=5, pady=5)   
        tk.Button(root, text="-", command=self.subtract).grid(row=0, column=3, padx=5, pady=5)
        tk.Button(root, text="*", command=self.multiply).grid(row=1, column=2,  padx=5, pady=5) 
        tk.Button(root, text="/", command=self.divide).grid(row=1, column=3, padx=5, pady=5)
    
    def get_numbers(self):
        try: # try - except giúp bắt lỗi khi người dùng nhập dữ liệu không phải là số (vẫn chạy khi xảy ra lỗi)
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return None, None
    
    def add(self):
        num1, num2 = self.get_numbers() 
        if num1 is not None: # kiểm tra xem người dùng đã nhập số vào ô input chưa
            self.result_entry.config(state='normal') # normal state giúp nguòi dùng nhập dữ liệu vào entry
            self.result_entry.delete(0, tk.END)     
            self.result_entry.insert(0, str(num1 + num2))
            self.result_entry.config(state='readonly')  # readonly state ngăn người dùng nhập dữ liệu vào entry
    
    def subtract(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            self.result_entry.config(state='normal')
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, str(num1 - num2))
            self.result_entry.config(state='readonly')
    
    def multiply(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            self.result_entry.config(state='normal')
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, str(num1 * num2))
            self.result_entry.config(state='readonly')
    
    def divide(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            if num2 == 0:
                messagebox.showerror("Math Error", "Cannot divide by zero.")
            else:
                self.result_entry.config(state='normal')
                self.result_entry.delete(0, tk.END)
                self.result_entry.insert(0, str(num1 / num2))
                self.result_entry.config(state='readonly')

if __name__ == "__main__":  
    root = tk.Tk() 
    app = CalculatorApp(root) 
    root.mainloop()