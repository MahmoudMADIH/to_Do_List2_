task_label = Label(functions_frame, text="Enter the Task:",
                   font=("arial", "14", "bold"),
                   background="black",
                   foreground="white"
                   )
task_label.place(x=20, y=30)

task_field = Entry(
    functions_frame,
    font=("Arial", "14"),
    width=42,
    foreground="black",
    background="white",
)
task_field.place(x=180, y=30)

add_button = Button(
    functions_frame,
    text="Add Task",
    width=15,
    bg='#D4AC0D', font=("arial", "14", "bold"),
    command=add_task,

)
del_button = Button(
    functions_frame,
    text="Delete Task",
    width=15,
    bg='#D4AC0D', font=("arial", "14", "bold"),
    command=delete_task,
)
del_all_button = Button(
    functions_frame,
    text="Delete All Tasks",
    width=15,
    font=("arial", "14", "bold"),
    bg='#D4AC0D',
    command=delete_all_tasks
)
exit_button = Button(
    functions_frame,
    text="Exit",
    width=52,
    bg='#D4AC0D', font=("arial", "14", "bold"),
    command=close
)
add_button.place(x=18, y=80, )
del_button.place(x=240, y=80)
del_all_button.place(x=460, y=80)
exit_button.place(x=17, y=330)

task_listbox = Listbox(
    functions_frame,
    width=57,
    height=7,
    font="bold",
    selectmode='SINGLE',
    background="WHITE",
    foreground="BLACK",
    selectbackground="#D4AC0D",
    selectforeground="BLACK"
)
task_listbox.place(x=17, y=140)

retrieve_database()
list_update()
guiWindow.mainloop()
the_connection.commit()
the_cursor.close()
