from asyncio import tasks
from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

<<<<<<< HEAD
=======



>>>>>>> 761987f (modified)
def add_task():
    task_string=task_field.get()
    if len(task_string)==0:
        messagebox.showinfo("error","the field is empty")
    else:
<<<<<<< HEAD
        task.append(task_string)
=======
        tasks.append(task_string)
>>>>>>> 761987f (modified)
        the_cursor.execute("insert the value (?)", task_string)
        list_update()
        task_delete(0,"end")
def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insart('end ', task)

<<<<<<< HEAD
def delete_task():
=======
def task_delete():
>>>>>>> 761987f (modified)
    try:
        the_value=task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
            the_cursor.execute("insert the value (?)", (the_value))
    except:
        messagebox.showinfo("error","no task selected. you can't delete")
def delete_all_tasks():
    message_box=messagebox.askyesno('delete all',"are you sure")
    if message_box==True :
        while (len(tasks)!=0):
            tasks.pop()
            the_cursor.execute("delete from tasks")
            list_update()
def clear_list():
    task_listbox.delete(0 ,'end')

def close ():
    print(tasks)
    guiWindow.destroy()

def retrieve_database():
    while (len(tasks)!=0):
        tasks.pop()
<<<<<<< HEAD
    for row in the_cursor.execute("select titele from tasks"):
        tasks.append(row[0])
=======

>>>>>>> 761987f (modified)


if __name__=="__main__":
    guiWindow=Tk()
    guiWindow.title("To Do List")
    guiWindow.geometry("665x400+550+250")
    guiWindow.resizable(0,0)
    guiWindow.configure(bg="#b5e5cf")
    The_connection=sql.connect('LastOfTasks.db')
    the_cursor=The_connection.cursor()
    the_cursor.execute('create table if not exists tasks (tittle_text)')
<<<<<<< HEAD
    task=[]
    function_frame=frame(guiWindow , bg='black')
    function_frame.pack(side='top' ,expand =True ,fill= "both")
=======
    tasks=[]
    function_frame=Frame(guiWindow , bg='black')
    function_frame.pack(side='top' ,expand =True ,fill= "both")
    task_label = Label(function_frame, text="Enter the Task:",
                       font=("arial", "14", "bold"),
                       background="black",
                       foreground="white"
                       )
    # using the place() method to place the label in the application
    task_label.place(x=20, y=30)

    # defining an entry field using the Entry() widget
    task_field = Entry(
        function_frame,
        font=("Arial", "14"),
        width=42,
        foreground="black",
        background="white",
    )
    # using the place() method to place the entry field in the application
    task_field.place(x=180, y=30)

    # adding buttons to the application using the Button() widget
    add_button = Button(
        function_frame,
        text="Add Task",
        width=15,
        bg='#D4AC0D', font=("arial", "14", "bold"),
        command=add_task,

    )
    del_button = Button(
        function_frame,
        text="Delete Task",
        width=15,
        bg='#D4AC0D', font=("arial", "14", "bold"),
        command=task_delete(),
    )
    del_all_button = Button(
        function_frame,
        text="Delete All Tasks",
        width=15,
        font=("arial", "14", "bold"),
        bg='#D4AC0D',
        command=delete_all_tasks
    )
    exit_button = Button(
        function_frame,
        text="Exit",
        width=52,
        bg='#D4AC0D', font=("arial", "14", "bold"),
        command=close
    )
    # using the place() method to set the position of the buttons in the application
    add_button.place(x=18, y=80, )
    del_button.place(x=240, y=80)
    del_all_button.place(x=460, y=80)
    exit_button.place(x=17, y=330)

    # defining a list box using the tk.Listbox() widget
    task_listbox = Listbox(
        function_frame,
        width=57,
        height=7,
        font="bold",
        selectmode='SINGLE',
        background="WHITE",
        foreground="BLACK",
        selectbackground="#D4AC0D",
        selectforeground="BLACK"
    )
    # using the place() method to place the list box in the application
    task_listbox.place(x=17, y=140)

    # calling some functions
    retrieve_database()
    list_update()
    # using the mainloop() method to run the application
    guiWindow.mainloop()
    # establishing the connection with database
    The_connection.commit()
    the_cursor.close()

>>>>>>> 761987f (modified)

