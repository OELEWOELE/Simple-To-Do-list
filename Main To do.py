import tkinter as tk

tasks = []

def add_task():
    task = task_entry.get()
    tasks.append(task)
    task_list.insert(tk.END, task)
    task_entry.delete(0, tk.END)

def view_tasks():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)

def delete_task():
    selected_task = task_list.get(task_list.curselection())
    tasks.remove(selected_task)
    view_tasks()

def edit_task():
    selected_task = task_list.get(task_list.curselection())
    index = tasks.index(selected_task)
    tasks[index] = task_entry.get()
    view_tasks()

root = tk.Tk()
root.title("To-Do List")

task_frame = tk.Frame(root)
task_frame.pack()

task_label = tk.Label(task_frame, text="Task:")
task_label.pack(side=tk.LEFT)

task_entry = tk.Entry(task_frame)
task_entry.pack(side=tk.LEFT)

add_button = tk.Button(task_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

task_list = tk.Listbox(root)
task_list.pack()

list_frame = tk.Frame(root)
list_frame.pack()

view_button = tk.Button(list_frame, text="View Tasks", command=view_tasks)
view_button.pack(side=tk.LEFT)

delete_button = tk.Button(list_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT)

edit_button = tk.Button(list_frame, text="Edit Task", command=edit_task)
edit_button.pack(side=tk.LEFT)

root.mainloop()
