import tkinter as tk
import pickle
import datetime

tasks = []

def add_task():
    task = task_entry.get()
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")
    tasks.append((task, current_date, False))
    task_list.insert(tk.END, f"{current_date} - {task}")
    task_entry.delete(0, tk.END)
    save_tasks()

def view_tasks():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task[0] + ' - ' + task[1])

def mark_as_complete():
    selected_index = task_list.curselection()
    if len(selected_index) > 0:
        selected_index = selected_index[0]
        task = tasks[selected_index]
        task = (task[0], task[1], True)
        tasks[selected_index] = task
        task_list.itemconfig(selected_index, {'fg': 'gray'})
        save_tasks()
    else:
        print("No task selected.")

def delete_task():
    selected_index = task_list.curselection()
    if len(selected_index) > 0:
        selected_index = selected_index[0]
        selected_task = tasks[selected_index]
        tasks.remove(selected_task)
        task_list.delete(selected_index)
        save_tasks()
    else:
        print("No task selected.")


def select_all(event=None):
    task_list.selection_clear(0, tk.END)
    task_list.selection_set(0, tk.END)

def save_tasks():
    with open("tasks.pickle", "wb") as f:
        pickle.dump(tasks, f)

def load_tasks():
    global tasks
    try:
        with open("tasks.pickle", "rb") as f:
            tasks = pickle.load(f)
    except:
        pass
def delete_all():
    task_list.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")
root.geometry("600x400")
root.bind("<Return>", lambda event: add_task())
root.bind("<BackSpace>", lambda event: delete_task())
root.bind('<Control-a>', select_all)

delete_all_button = tk.Button(root, text="Delete All", command=delete_all)
delete_all_button.grid(row=0, column=0, padx=5, pady=5)

task_frame = tk.Frame(root)
task_frame.grid(row=1, column=0, sticky="W", padx=5, pady=5)

task_label = tk.Label(task_frame, text="Task:")
task_label.grid(row=0, column=0, sticky="W")

task_entry = tk.Entry(task_frame)
task_entry.grid(row=0, column=1, sticky="W", padx=5)

task_list = tk.Listbox(root)
task_list.grid(row=2, column=0, columnspan=2, sticky="nsew")

scrollbar = tk.Scrollbar(task_list, orient="vertical")
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.config(command=task_list.yview)
task_list.config(yscrollcommand=scrollbar.set)

list_frame = tk.Frame(root)
list_frame.grid(row=3, column=0, sticky="w")

view_button = tk.Button(list_frame, text="View Tasks", command=view_tasks)
view_button.grid(row=0, column=0, padx=5, pady=5)

complete_button = tk.Button(list_frame, text="Complete Task", command=mark_as_complete)
complete_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(list_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=2, padx=5, pady=5)

root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

load_tasks()
root.mainloop()