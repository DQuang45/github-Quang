import tkinter as tk
from tkinter import messagebox
import re # thư viện hỗ trợ kiểm tra định dạng email

class FormLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        
        tk.Label(self.root, text="Username:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=0, column=1)
        
        tk.Label(self.root, text="Password:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1)

        self.show_password = tk.BooleanVar() # thêm biến show_password để lưu trạng thái hiển thị mật khẩu
        self.show_password_button = tk.Checkbutton(self.root, text="Show Password", variable=self.show_password, command=self.toggle_password)
        self.show_password_button.grid(row=2, column=2, sticky="w") # sticky="w" giúp căn chỉnh checkbox về phía tây
        
        tk.Button(self.root, text="Login", command=self.login).grid(row=2, column=0, columnspan=2)
    def toggle_password(self): # thêm hàm toggle_password để hiển thị hoặc ẩn mật khẩu
        if self.show_password.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if not username or not password:
            messagebox.showerror("Input Error", "Both fields are required.")
            return
        
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", username): # kiểm tra định dạng email
            messagebox.showerror("Input Error", "Invalid username format.")
            return

        # Giả lập kiểm tra tài khoản (bạn có thể thay bằng kiểm tra từ cơ sở dữ liệu)
        if username == "admin@123" and password == "Abe1123":
            messagebox.showinfo("Login Success", "Welcome!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

if __name__ == "__main__":
    root = tk.Tk()
    app = FormLogin(root)
    root.mainloop()
