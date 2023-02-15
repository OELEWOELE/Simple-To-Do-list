import tkinter as tk
import pickle
import datetime

tasks = []
#defining all the functions(clickable buttons)
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
#adding the root for the definitions
root = tk.Tk()
root.title("To-Do List")
root.geometry("600x400")
root.bind("<Return>", lambda event: add_task())
root.bind("<BackSpace>", lambda event: delete_task())

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

complete_button = tk.Button(list_frame, text="Complete Task", command=mark_as_complete)
complete_button.pack(side=tk.LEFT)

delete_button = tk.Button(list_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.RIGHT)

root.mainloop()
