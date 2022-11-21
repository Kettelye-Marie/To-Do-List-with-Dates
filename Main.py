#establish GUI elements
import tkinter
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry

#create root window
root = tkinter.Tk()
root.configure(bg = "SteelBlue4")
root.title("ToDo List")
root.geometry("400x350")
#create empty lists
tasks = []
dates = []

def update_listbox():
    # clear the current listbox
    clear_listbox()
    # Populate listbox by appending each task to list
    for task in tasks:
        lb_tasks.insert("end", task)
    # Populate listbox by appending dates to list
    for date in dates:
        lb_dates.insert("end", date)

def clear_listbox():
    lb_tasks.delete(0, "end")
    lb_dates.delete(0,"end")

def add_task(event=None): # "event=None" so that enter key can add task without clicking the button
    #get user input(prompt)
    task = txt_input.get()
    # Ensure user has enetered a task
    if task !="":
      tasks.append(task)
      #capturing the date associated with entered task
      dates.append(cal.get_date())
      update_listbox()
    else:
        messagebox.showwarning("Note!", "Please enter a task")
    # Clear the textbox to avoid adding the same task twice accidentally
    txt_input.delete(0, "end")

root.bind('<Return>', add_task)# bind return key to add_task so that enter key can add task without clicking the button


def delete_task():

    # Get the text of the currently selected item
    task = lb_tasks.get("active")
    # Confirm task is in list
    if task in tasks:
        confirm_del = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete task:   ** {} ** ?".format(task))
        if confirm_del:# tkmessageBox.askyesno returns boolean
            #deletes the date at the same index of the task
            del dates[tasks.index(task)]
            tasks.remove(task)
    update_listbox()


def sort_list_up():
    tasks.sort()
    update_listbox()

def sort_list_down():
    tasks.sort()
    tasks.reverse()
    update_listbox()


def delete_all():
    # As list is being changed, it needs to be global.
    global tasks
    confirm_del = messagebox.askyesno("Delete All Confirmation", "Are you sure you want to delete all tasks?")
    if confirm_del:
      # Clears the lists.
      tasks = []
      dates = []
      # Update listbox
      update_listbox()

def exit():
    quit()

#Creating and formatting the GUI elemets

txt_input = tkinter.Entry(root, width = 15)
txt_input.grid(row=1 , column=1 )

btn_add_task = tkinter.Button(root, text="Add Task", fg="black", bg="SpringGreen3", command=add_task)
btn_add_task.grid(row= 1, column=0 )

btn_delete_task = tkinter.Button(root, text="Delete Task", fg="black", bg="indianred", command=delete_task)
btn_delete_task.grid(row=4 , column=0 )

btn_delete_all = tkinter.Button(root, text="Delete All", fg="black", bg="indianred", command=delete_all)
btn_delete_all.grid(row=5 , column= 0)

btn_sort_list_up = tkinter.Button(root, text="Sort List Ascending", fg="black", bg="LightSkyBlue1", command=sort_list_up)
btn_sort_list_up.grid(row=6 , column=0 )

btn_sort_list_down = tkinter.Button(root, text="Sort List Descending", fg="black", bg="LightSkyBlue1", command=sort_list_down)
btn_sort_list_down.grid(row=7 , column=0 )

btn_quit_program = tkinter.Button(root, text="Exit", fg="black", bg="white", command=exit)
btn_quit_program.grid(row=9 , column=0 )

lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=3 , column=1, rowspan=7 )

lb_dates = tkinter.Listbox(root)
lb_dates.grid(row=3 , column=3, rowspan=7 )

#Create calendar selector
cal = DateEntry(root, width= 12, background= "DodgerBlue4", foreground= "white",bd=2)
cal.grid(row=1, column=3)

# Start the main events loop
root.mainloop()