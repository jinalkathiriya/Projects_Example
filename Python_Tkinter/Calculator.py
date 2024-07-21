import tkinter as tk
from tkinter import ttk

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.num1_label = tk.Label(root, text="Enter the first number:")
        self.num1_label.pack(pady=5)
        self.num1_entry = tk.Entry(root)
        self.num1_entry.pack(pady=5)

        self.num2_label = tk.Label(root, text="Enter the second number:")
        self.num2_label.pack(pady=5)
        self.num2_entry = tk.Entry(root)
        self.num2_entry.pack(pady=5)

        self.operation_label = tk.Label(root, text="Choose an operation:")
        self.operation_label.pack(pady=5)
        self.operation_var = tk.StringVar()
        self.operation_menu = ttk.Combobox(root, textvariable=self.operation_var, values=["Addition", "Subtraction", "Multiplication", "Division"])
        self.operation_menu.pack(pady=5)
        self.operation_menu.current(0)

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.pack(pady=5)

        self.progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
        self.progress.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=5)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            self.progress.start()
            self.root.after(1000, self.show_result, num1, num2, operation)

        except ValueError:
            self.result_label.config(text="Invalid input. Please enter numbers.")

    def show_result(self, num1, num2, operation):
        self.progress.stop()
        
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                self.result_label.config(text="Error! Division by zero.")
                return
        else:
            self.result_label.config(text="Invalid operation.")
            return

        self.result_label.config(text=f"Result: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()
