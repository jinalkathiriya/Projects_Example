import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from time import strftime

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.todo_list = {}

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack()

        self.calendar = Calendar(root, selectmode="day", year=2024, month=7, day=3)
        self.calendar.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=40, height=10)
        self.task_listbox.pack()

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.time_label = ttk.Label(root, font=('calibri', 40, 'bold'), background='blue', foreground='white')
        self.time_label.pack()

        self.update_time()

    def add_task(self):
        task = self.task_entry.get()
        task_date = self.calendar.selection_get()
        if task_date in self.todo_list:
            self.todo_list[task_date].append(task)
        else:
            self.todo_list[task_date] = [task]
        self.task_listbox.insert(tk.END, f"{task_date}: {task}")
        self.task_entry.delete(0, tk.END)

    def update_task(self):
        task_date = self.calendar.selection_get()
        task_number = int(self.task_listbox.curselection()[0])
        new_task = self.task_entry.get()
        self.todo_list[task_date][task_number] = new_task
        self.task_listbox.delete(task_number)
        self.task_listbox.insert(task_number, f"{task_date}: {new_task}")
        self.task_entry.delete(0, tk.END)

    def delete_task(self):
        task_date = self.calendar.selection_get()
        task_number = int(self.task_listbox.curselection()[0])
        del self.todo_list[task_date][task_number]
        self.task_listbox.delete(task_number)
        self.task_entry.delete(0, tk.END)

    def update_time(self):
        string = strftime('%H:%M:%S %p')
        self.time_label.config(text=string)
        self.time_label.after(1000, self.update_time)

root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()