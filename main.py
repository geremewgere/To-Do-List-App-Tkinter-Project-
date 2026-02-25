import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks():
    listbox.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("350x400")

# Entry
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10, padx=10, fill=tk.X)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete Task", width=12, command=delete_task)
delete_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear All", width=12, command=clear_tasks)
clear_btn.grid(row=0, column=2, padx=5)

# Listbox
listbox = tk.Listbox(root, font=("Arial", 14))
listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

root.mainloop()
