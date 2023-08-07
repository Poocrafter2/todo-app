import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_task(), key='todos',
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box,add_button,complete_button],[list_box,edit_button]],
                   font=('Helvitica', 15))
while True:
    event, values = window.read()
    print(event)
    print(values)
    print("hello")
    match event:
        case "Add":
            todos = functions.get_task()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_task(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_task()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_task(todos)
            window['todos'].update(values=todos)

        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()