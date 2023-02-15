import tkinter as tk
import pickle
import datetime

class Task:
    def __init__(self, task, date, complete=False):
        self.task = task
        self.date = date
        self.complete = complete

root = tk.Tk()
todo = ToDoList(root)
root.mainloop()

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("600x400")
        self.root.bind("<Return>", self.add_task)
        self.root.bind("<BackSpace>", self.delete_task)
        self.root.bind('<Control-a>', self.select_all)

        self.tasks = []
        self.load_tasks()

        self.create_widgets()

    def create_widgets(self):
        delete_all_button = tk.Button(self.root, text="Delete All", command=self.delete_all)
        delete_all_button.grid(row=0, column=0, padx=5, pady=5)

        task_frame = tk.Frame(self.root)
        task_frame.grid(row=1, column=0, sticky="W", padx=5, pady=5)

        task_label = tk.Label(task_frame, text="Task:")
        task_label.grid(row=0, column=0, sticky="W")

        self.task_entry = tk.Entry(task_frame)
        self.task_entry.grid(row=0, column=1, sticky="W", padx=5)

        self.task_list = tk.Listbox(self.root)
        self.task_list.grid(row=2, column=0, columnspan=2, sticky="nsew")

        self.scrollbar = tk.Scrollbar(self.task_list, orient="vertical")
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar.config(command=self.task_list.yview)
        self.task_list.config(yscrollcommand=self.scrollbar.set)

        self.list_frame = tk.Frame(self.root)
        self.list_frame.grid(row=3, column=0, sticky="w")

        self.view_button = tk.Button(self.list_frame, text="View Tasks", command=self.view_tasks)
        self.view_button.grid(row=0, column=0, padx=5, pady=5)

        self.complete_button = tk.Button(self.list_frame, text="Complete Task", command=self.mark_as_complete)
        self.complete_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = tk.Button(self.list_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5, pady=5)

        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.task_list.grid(row=2, column=0, sticky="nsew")

        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.task_list.yview)
        scrollbar.grid(row=2, column=1, sticky="ns")

        self.task_list.configure(yscrollcommand=scrollbar.set)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=3, column=0, pady=10)

        self.root.mainloop()

