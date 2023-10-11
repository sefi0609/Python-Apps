import app1
import PySimpleGUI as sg

layout = [[sg.InputText(size=42, tooltip='Enter todo: ')],
          [sg.Multiline(size=(40, 5), key='textbox')],
          [sg.Button('Add'), sg.Button('Show'), sg.Button('Edit'), sg.Button('Complete'), sg.Button('Exit')]]

window = sg.Window('My To-Do App', layout)
event, values = window.read()
# output = app1.todo_list(event)

window.close()
