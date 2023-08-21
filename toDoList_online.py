from tkinter import *
from tkinter import messagebox
import sqlite3 as sql


def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values (?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')


def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)


def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
            the_cursor.execute('delete from tasks where title = ?', (the_value,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')


def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box == True:
        while (len(tasks) != 0):
            tasks.pop()
        the_cursor.execute('delete from tasks')
        list_update()


def clear_list():
    task_listbox.delete(0, 'end')


def close():
    print(tasks)
    guiWindow.destroy()


def retrieve_database():
    while (len(tasks) != 0):
        tasks.pop()


if __name__ == "__main__":
    guiWindow = Tk()
    guiWindow.title("To-Do List ")
    guiWindow.geometry("665x400+550+250")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#B5E5CF")

    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title_text)')

    tasks = []

    functions_frame = Frame(guiWindow, bg="black")

    functions_frame.pack(side="top", expand=True, fill="both")

    task_label = Label(functions_frame, text="Enter the task",
                       font=("arial", 14, "bold"),
                       background="black",
                       foreground="white")
    task_label.place(x=20, y=30)

    task_field = Entry(functions_frame,
                       font=("arial", 14),
                       width=42,
                       background="white",
                       foreground="black")
    task_field.place(x=180, y=30)

    add_button = Button(functions_frame,
                        font=("arial", 14, "bold"),
                        width=15,
                        text="add task",
                        command=add_task,
                        bg='#D4AC0D')
    del_button = Button(functions_frame,
                        font=("arial", 14, "bold"),
                        width=15,
                        bg='#D4AC0D',
                        text="delete_task",
                        command=delete_task)
    del__all_button = Button(functions_frame,
                             font=("arial", 14, "bold"),
                             width=15,
                             bg='#D4AC0D',
                             text="delete All task",
                             command=delete_all_tasks)
    exit_button = Button(functions_frame,
                         font=("arial", 14, "bold"),
                         width=52,
                         bg='#D4AC0D',
                         text="Exit",
                         command=close)
    add_button.place(x=18, y=80)
    del_button.place(x=240, y=80)
    del__all_button.place(x=460, y=80)
    exit_button.place(x=17, y=330)

    task_listbox = Listbox(functions_frame,
                           font=('bold'),
                           width=57,
                           height=7,
                           selectmode='SINGEL',
                           background='WHITE',
                           foreground='BLACK',
                           selectbackground='#D4AC0D',
                           selectforeground='WHITE')
    task_listbox.place(x=17, y=140)

    retrieve_database()
    list_update()
    guiWindow.mainloop()
    the_connection.commit()
    the_cursor.close()
