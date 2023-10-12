import app1
import time
import PySimpleGUI as sg

sg.theme('BlueMono')

initial_prompt = """To edit or complete a todo list item,
Please enter a line number and then press the matching button
"""

layout = [[sg.Text('', size=(10, 1), font=('Any', 25), key='timetext')],
          [sg.Text('Type in a to-do')],
          [sg.InputText(size=42, tooltip='Enter todo: ', key='textinput')],
          [sg.Multiline(initial_prompt, size=(40, 6), key='textbox')],
          [sg.Button('Add'), sg.Button('Show'), sg.Button('Edit'), sg.Button('Complete'), sg.Button('Exit')]]


def todo():
    """ Main entry point - deals with all the possible commends """
    window = sg.Window('My To-Do App', layout)
    while True:
        event, values = window.read(timeout=10)
        window['timetext'].update(time.strftime('%H:%M:%S'))
        # two ways to exit the application
        if event in [sg.WINDOW_CLOSED, 'Exit']:
            break
        # handel the current user action
        match event:
            case 'Show':
                output = app1.show()
                window['textbox'].update(output)
                window['textinput'].update('')
            case 'Add':
                if values['textinput'] != '':
                    output = app1.add(values['textinput'])
                    window['textbox'].update(output)
                    window['textinput'].update('')
            case 'Edit':
                try:
                    # check if the number entered is a line in the to-do list
                    if app1.is_valid_number(int(values['textinput'])):
                        # get the edited line
                        text = sg.popup_get_text('Enter The edited line', title="Waiting You Response")
                        if text:
                            output = app1.edit(int(values['textinput']), text)
                            # show the output
                            window['textbox'].update(output)
                    # if the number is not valid
                    else:
                        window['textbox'].update('Invalid number, Please try again')
                # if the user didn't enter a number
                except ValueError:
                    window['textbox'].update('Please enter a number: ')
                window['textinput'].update('')
            case 'Complete':
                try:
                    output = app1.complete(int(values['textinput']))
                    window['textbox'].update(output)
                except ValueError:
                    window['textbox'].update('Please enter a number: ')
                window['textinput'].update('')

    window.close()


if __name__ == '__main__':
    todo()
