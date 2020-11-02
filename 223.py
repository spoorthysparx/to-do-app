import PySimpleGUI as sg

todolist=[]
low,medium,high = [],[],[]
sg.theme("BluePurple")
layout=[
    [sg.Text("enter your choice",font=("Arial",16)),
    sg.In("",size=(20,1),font=("Arial",16),key="choice"),
    sg.Button("Add",key="add_save"),
    sg.Button("save task",key="save_tasks"),
    sg.Button("show tasks",key="show_tasks")
    ],
    [sg.Listbox([],size=(70,5),font=("Arial",16),key="tasks"),
    sg.InputCombo(["high","medium","low"],"choose the priority",size=(20,3),
    font=("Arial",16),key="priority"),
    sg.Button("Edit",key="edit"),
    sg.Button("Delete",key="delete")
    ],
    [sg.Button("exit",key="exit")],
    [sg.Text('Calendar')],
    [sg.In(key='date', enable_events=True, visible=False),
     sg.CalendarButton('Calendar', target='date',
    button_color=('black', 'white'), key='cal', format=('%d %B, %Y'))]     
]

def add_tasks(values):
    choice=values['choice']
    priority=values['priority']
    todolist.append({'task':choice,'priority':priority})
    window.FindElement('tasks').update(values=todolist)
    window.FindElement('choice').update(value='')
    window.FindElement("add_save").update("add")

def delete_tasks(values):
    tasks=values['tasks'][0]
    todolist.remove(tasks)
    with open("122.txt", "r") as f:
        lines = f.readlines()
    with open("122.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != tasks:
                f.write(line)
    window.FindElement('tasks').update(values=todolist)

def edit_tasks(values):
    edited_val=values['tasks'][0]
    window.FindElement('choice').update(value=edited_val)
    todolist.remove(edited_val)
    window.FindElement('add_save').update('save')

def set_deadline(values):
    selected_task=values['tasks'][0]
    for i in range(len(todolist)): 
        if todolist[i]['task'] == values['tasks'][0]['task']: 
            del todolist[i] 
            break
    selected_task["deadline"]= values['date']
    todolist.append(selected_task)
    window.FindElement('tasks').update(values=todolist)


def save_tasks():
    for i in todolist:
            if i['priority'] == "high":
                high.append([i['task'],i['priority'],i['deadline']])
            elif i['priority'] == "medium":
                medium.append([i['task'],i['priority'],i['deadline']])
            elif i['priority'] == "low":
                low.append([i['task'],i['priority'],i['deadline']])
    print(high)                              
    with open('122.txt','w') as f:
        for i in high:
            f.writelines(i[0]+'\t' + i[1]+'\t'+ i[2])
        for i in medium:
            f.writelines(i[0]+'\t' + i[1]+'\t'+ i[2])
        for i in low:
            f.writelines(i[0]+'\t' + i[1]+'\t'+ i[2])            
    todolist.clear()  

def show_tasks():
    with open('122.txt','r') as f:
        task=f.readlines()
        for i in task:
            if i not in todolist:
                    todolist.append(i.split())
    window.FindElement("tasks").update(todolist)

window= sg.Window("first app",layout)
while True:
    event,values=window.read()
    if event=="add_save":
        add_tasks(values)
    elif event=="delete":
        delete_tasks(values)
    elif event=="edit":
        edit_tasks(values)
    elif event == "save_tasks":
        save_tasks()
    elif event=="show_tasks":
        show_tasks()
    elif event == "date":
        set_deadline(values)    
    else:
        break
window.close()