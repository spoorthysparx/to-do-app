import PySimpleGUI as sg

layout=[
    [sg.Text("enter your choice",font=("Arial",16)),
    sg.InputText("",size=(20,1),font=("Arial",16),key="choice"),sg.Button("Add",key="add_save")],
    [sg.Listbox([],size=(40,5),font=("Arial",16),key="tasks"),
    sg.Button("Edit",key="edit"),sg.Button("Delete",key="delete"),],[sg.Button("exit",key="exit")]
]

def add_tasks(values):
    choice=values['choice']
    todolist.append(choice)
    window.FindElement('tasks').update(values=todolist)
    window.FindElement('choice').update(value='')
    window.FindElement("add_save").update("add")

def delete_tasks(values):
    tasks=values['tasks'][0]
    todolist.remove(tasks)
    window.FindElement('tasks').update(values=todolist)

def edit_tasks(values):
    edited_val=values['tasks'][0]
    window.FindElement('choice').update(value=edited_val)
    todolist.remove(edited_val)
    window.FindElement('add_save').update('save')

todolist=[]

window= sg.Window("first app",layout)
while True:
    event,values=window.read()
    if event=="add_save":
        add_tasks(values)
    elif event=="delete":
        delete_tasks(values)
    elif event=="edit":
        edit_tasks(values)
    else:
        break
window.close()