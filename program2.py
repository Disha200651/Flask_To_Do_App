import tkinter as tk
from tkinter import messagebox

# List to hold tasks
tasks = []


# Add a new task
def add_task():
    task = entry.get()
    if task:
        tasks.append({"name": task, "done": False})
        entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")


# Mark selected task as done
def mark_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = True
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task.")


# Delete selected task
def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task.")


# Update the listbox
def update_task_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔️ Done" if task["done"] else "❌ Not Done"
        listbox.insert(tk.END, f"{task['name']} [{status}]")


# Main window
root = tk.Tk()
root.title("🖊️To-Do List App 📝")
root.geometry("400x500")  # Set a fixed window size
root.configure(bg="#f9f9f9")  # Light background color

# Entry field
entry = tk.Entry(root, font=("Helvetica", 14), bd=2, relief=tk.GROOVE)
entry.pack(pady=15, padx=20, fill=tk.X)

# Buttons
btn_frame = tk.Frame(root, bg="#f9f9f9")
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="➕ Add Task", command=add_task,
                    font=("Helvetica", 12), bg="#4CAF50", fg="white", relief=tk.RAISED, bd=2)
add_btn.pack(side=tk.LEFT, padx=5)

mark_done_btn = tk.Button(btn_frame, text="✔️ Mark Done", command=mark_done,
                           font=("Helvetica", 12), bg="#2196F3", fg="white", relief=tk.RAISED, bd=2)
mark_done_btn.pack(side=tk.LEFT, padx=5)

delete_btn = tk.Button(btn_frame, text="❌ Delete Task", command=delete_task,
                        font=("Helvetica", 12), bg="#F44336", fg="white", relief=tk.RAISED, bd=2)
delete_btn.pack(side=tk.LEFT, padx=5)

# Listbox
listbox = tk.Listbox(root, font=("Times New Roman", 12), selectbackground="#B3E5FC",
                     selectforeground="black", bd=2, relief=tk.SUNKEN, height=15)
listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

# Run the app
root.mainloop()
