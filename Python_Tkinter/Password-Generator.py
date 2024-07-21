import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root, text="Enter the desired password length:")
        self.length_label.pack(pady=5)
        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=5)

        self.complexity_label = tk.Label(root, text="Select password complexity:")
        self.complexity_label.pack(pady=5)
        self.complexity_var = tk.IntVar()
        self.complexity_var.set(1)
        self.complexity_frame = tk.Frame(root)
        self.complexity_frame.pack(pady=5)
        tk.Radiobutton(self.complexity_frame, text="Low (Lowercase letters)", variable=self.complexity_var, value=1).pack(anchor='w')
        tk.Radiobutton(self.complexity_frame, text="Medium (Lowercase + Uppercase)", variable=self.complexity_var, value=2).pack(anchor='w')
        tk.Radiobutton(self.complexity_frame, text="High (Letters + Digits)", variable=self.complexity_var, value=3).pack(anchor='w')
        tk.Radiobutton(self.complexity_frame, text="Very High (Letters + Digits + Special Characters)", variable=self.complexity_var, value=4).pack(anchor='w')

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=5)

        self.password_label = tk.Label(root, text="", font=("Arial", 14))
        self.password_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            complexity = self.complexity_var.get()

            if complexity == 1:
                characters = string.ascii_lowercase
            elif complexity == 2:
                characters = string.ascii_letters
            elif complexity == 3:
                characters = string.ascii_letters + string.digits
            elif complexity == 4:
                characters = string.ascii_letters + string.digits + string.punctuation
            else:
                self.password_label.config(text="Invalid complexity level.")
                return

            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_label.config(text=f"Generated Password: {password}")

        except ValueError:
            self.password_label.config(text="Invalid input. Please enter a valid number for the length.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
