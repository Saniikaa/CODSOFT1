import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    title = entry_title.get()
    if title:
        tasks.append({"title": title, "completed": False})
        update_task_list()
        entry_title.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task title cannot be empty!")

def remove_task():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "No task selected to remove!")

def update_task_list():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        status = "✓" if task["completed"] else "✗"
        listbox_tasks.insert(tk.END, f"{task['title']} [{status}]")

def mark_task_completed():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        tasks[selected_task[0]]["completed"] = True
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "No task selected to mark completed!")



# GUI setup
root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry_title = tk.Entry(frame, width=30)
entry_title.pack(side=tk.LEFT, padx=5)
btn_add = tk.Button(frame, text="Add Task", command=add_task)
btn_add.pack(side=tk.LEFT)

listbox_tasks = tk.Listbox(root, width=50, height=15)
listbox_tasks.pack(pady=10)

btn_complete = tk.Button(root, text="Mark Completed", command=mark_task_completed)
btn_complete.pack(pady=5)

btn_remove = tk.Button(root, text="Remove Task", command=remove_task)
btn_remove.pack(pady=5)

root.mainloop()
