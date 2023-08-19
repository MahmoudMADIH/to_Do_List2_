from asyncio import tasks
from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task_string=task_field.get()
    if len(task_string)==0:
        messagebox.showinfo("error","the field is empty")
    else:
        task.append(task_string)
        the_cursor.execute("insert the value (?)", task_string)
        list_update()
        task_delete(0,"end")
def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insart('end ', task)

def delete_task():
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
    for row in the_cursor.execute("select titele from tasks"):
        tasks.append(row[0])


if __name__=="__main__":
    guiWindow=Tk()
    guiWindow.title("To Do List")
    guiWindow.geometry("665x400+550+250")
    guiWindow.resizable(0,0)
    guiWindow.configure(bg="#b5e5cf")
    The_connection=sql.connect('LastOfTasks.db')
    the_cursor=The_connection.cursor()
    the_cursor.execute('create table if not exists tasks (tittle_text)')
    task=[]
    function_frame=frame(guiWindow , bg='black')
    function_frame.pack(side='top' ,expand =True ,fill= "both")

