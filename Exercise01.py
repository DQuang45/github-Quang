import tkinter as tk
from tkinter import messagebox # hiển thị thông báo pop-up khi người dùng nhấn "Submit"

class SurveyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Programming Survey")
        
        # Question 1: Programming languages
        self.languages = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go"]
        self.language_vars = {}
        tk.Label(root, text="Which programming languages do you know?").pack(anchor="w")
        for lang in self.languages:
            var = tk.BooleanVar()
            self.language_vars[lang] = var
            tk.Checkbutton(root, text=lang, variable=var).pack(anchor="w")
        
        # Question 2: Experience level
        self.experience_var = tk.StringVar(value="Beginner")
        tk.Label(root, text="How experienced are you?").pack(anchor="w")
        for level in ["Beginner", "Intermediate", "Advanced"]:
            tk.Radiobutton(root, text=level, variable=self.experience_var, value=level).pack(anchor="w")
        
        # Submit button
        tk.Button(root, text="Submit", command=self.show_results).pack(pady=10)
    
    def show_results(self):
        selected_languages = [lang for lang, var in self.language_vars.items() if var.get()]
        experience_level = self.experience_var.get()
        
        result_text = "Survey Results:\n"
        result_text += f"Languages Known: {', '.join(selected_languages) if selected_languages else 'None'}\n"
        result_text += f"Experience Level: {experience_level}"
        
        messagebox.showinfo("Survey Results", result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = SurveyApp(root)
    root.mainloop()
