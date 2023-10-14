import app1
import PySimpleGUI as sg
import time
import threading

sg.theme('BlueMono')

layout = [[sg.Text('', size=(18, 1), font=('Any', 25), key='clock')],
          [sg.Text('Type in a to-do:')],
          [sg.InputText(size=45, tooltip='Enter todo: ', key='textinput'), sg.Button('Add')],
          [sg.Listbox(values=app1.read_from_file(), size=(35, 10), key='listbox', enable_events=True),
           sg.Button('Edit')],
          [sg.Button('Complete'), sg.Button('Reset'), sg.Button('Exit')]]


def popup_thread(window: sg.Window, text):
    """ release a popup thread """
    window.write_event_value('-POPUP-', text)


def todo():
    """ Main entry point - deals with all the possible commends """
    # allocate all the wights in the window - center
    window = sg.Window('My To-Do App', layout, element_justification='c')
    while True:
        # clock configuration
        event, values = window.read(timeout=100)
        window['clock'].update(time.strftime('%b %d %Y - %H:%M:%S'))
        output = None

        # two ways to exit the application
        if event in [sg.WINDOW_CLOSED, 'Exit']:
            break

        # handel the current user action
        match event:
            case 'Add':
                # if the user didn't enter a new line
                if values['textinput'] != '':
                    output = app1.add(values['textinput'])
                    window['listbox'].update(app1.read_from_file())
                    window['textinput'].update('')
                else:
                    output = 'Please enter a new line'

            case 'Edit':
                try:
                    # if a line is not selected the next line will cause an exception
                    output = app1.edit(values['listbox'][0], values['textinput'])
                    window['listbox'].update(app1.read_from_file())
                    window['textinput'].update('')
                except IndexError:
                    output = 'Please select an item to edit'

            case 'Complete':
                try:
                    # if a line is not selected the next line will cause an exception
                    app1.complete(values['listbox'][0])
                    window['listbox'].update(app1.read_from_file())
                    window['textinput'].update('')
                except IndexError:
                    output = 'Please select an item to complete'

            case 'Reset':
                # reset the application to initial state
                window['textinput'].update('')
                window['listbox'].update(app1.read_from_file())

            # new popup thread
            case '-POPUP-':
                sg.popup_non_blocking(values['-POPUP-'], title='Popup Message')

            # write the selected item into the text input
            case 'listbox':
                try:
                    window['textinput'].update(values['listbox'][0])
                except IndexError:
                    output = 'Please add items to your list'

        # popup a relevant message
        if output:
            threading.Thread(target=popup_thread, args=(window, output), daemon=True).start()

    window.close()


if __name__ == '__main__':
    todo()
