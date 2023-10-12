import app1
import PySimpleGUI as sg
import time
import threading

sg.theme('BlueMono')

initial_prompt = """To edit or complete a todo list item,
Please enter a line number and then press the matching button
"""

layout = [[sg.Text('', size=(10, 1), font=('Any', 25), key='timetext')],
          [sg.Text('Type in a to-do')],
          [sg.InputText(size=47, tooltip='Enter todo: ', key='textinput'), sg.Button('Add')],
          [sg.Listbox(values=app1.read_from_file(), size=(45, 10), key='listbox'), sg.Button('Edit')],
          [sg.Button('Complete'), sg.Button('Exit')]]


def todo():
    """ Main entry point - deals with all the possible commends """
    window = sg.Window('My To-Do App', layout)
    while True:
        # clock configuration
        event, values = window.read()
        window['timetext'].update(time.strftime('%H:%M:%S'))
        # two ways to exit the application
        if event in [sg.WINDOW_CLOSED, 'Exit']:
            break
        # handel the current user action
        match event:
            case 'Add':
                if values['textinput'] != '':
                    # need to release a thread for output popup
                    output = app1.add(values['textinput'])
                    window['listbox'].update(app1.read_from_file())
                    window['textinput'].update('')
            case 'Edit':
                text = sg.popup_get_text('Enter The edited line: ', title="Waiting You Response")
                # need to release a thread for output popup
                output = app1.edit(values['listbox'][0], text)
                window['listbox'].update(app1.read_from_file())
            case 'Complete':
                # need to release a thread for output popup
                output = app1.complete(values['listbox'][0])
                window['listbox'].update(app1.read_from_file())

    window.close()


if __name__ == '__main__':
    todo()
