import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter todo", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box,add_button,edit_button,complete_button]],
                   font=('Helvitica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_task()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_task(todos)
        case sg.WIN_CLOSED:
            break

window.close()