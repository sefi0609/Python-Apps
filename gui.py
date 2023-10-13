import app1
import PySimpleGUI as sg
import time
import threading

sg.theme('BlueMono')

initial_prompt = """To edit or complete a todo list item,
Please enter a line number and then press the matching button
"""

layout = [[sg.Text('', size=(7, 1), font=('Any', 25), key='timetext')],
          [sg.Text('Type in a to-do:')],
          [sg.InputText(size=45, tooltip='Enter todo: ', key='textinput'), sg.Button('Add')],
          [sg.Listbox(values=app1.read_from_file(), size=(35, 10), key='listbox', enable_events=True), sg.Button('Edit')],
          [sg.Button('Complete'), sg.Button('Exit')]]


def popup_thread(window: sg.Window, text):
    """ release a popup thread """
    window.write_event_value('-POPUP-', text)


def todo():
    """ Main entry point - deals with all the possible commends """
    # allocate all the wights in the window - center
    window = sg.Window('My To-Do App', layout, element_justification='c')
    while True:
        # clock configuration
        event, values = window.read(timeout=10)
        window['timetext'].update(time.strftime('%H:%M:%S'))
        output = None

        # two ways to exit the application
        if event in [sg.WINDOW_CLOSED, 'Exit']:
            break

        # handel the current user action
        match event:
            case 'Add':
                if values['textinput'] != '':
                    output = app1.add(values['textinput'])
                    window['listbox'].update(app1.read_from_file())
                    window['textinput'].update('')
                else:
                    output = 'Please enter a new line'

            case 'Edit':
                if values['listbox']:
                    # if the user press cancel in the popup - do nothing
                    output = app1.edit(values['listbox'][0], values['textinput'])
                    window['listbox'].update(app1.read_from_file())
                    window['textinput'].update('')
                else:
                    output = 'Please select an item to edit'

            case 'Complete':
                if values['listbox']:
                    app1.complete(values['listbox'][0])
                    window['listbox'].update(app1.read_from_file())
                    window['textinput'].update('')
                else:
                    output = 'Please select an item to complete'

            # new popup thread
            case '-POPUP-':
                sg.popup_non_blocking(values['-POPUP-'], title='Popup Message')

            # write the selected item into the text input
            case 'listbox':
                window['textinput'].update(values['listbox'][0])

        # popup a relevant message
        if output:
            threading.Thread(target=popup_thread, args=(window, output), daemon=True).start()

    window.close()


if __name__ == '__main__':
    todo()
