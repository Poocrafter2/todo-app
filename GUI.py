import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
window = sg.Window('My To-Do App', layout=[[label], [input_box,add_button,edit_button,complete_button]])

window.read()
window.close()