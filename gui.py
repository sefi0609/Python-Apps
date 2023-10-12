import app1
import PySimpleGUI as sg

initial_prompt = """To edit or complete a todo list item,
Please enter a line number and then press the matching button
"""

layout = [[sg.Text('Type in a to-do')],
          [sg.InputText(size=42, tooltip='Enter todo: ', key='textinput')],
          [sg.Multiline(initial_prompt, size=(40, 6), key='textbox')],
          [sg.Button('Add'), sg.Button('Show'), sg.Button('Edit'), sg.Button('Complete')]]


def todo():
    """ Main entry point - deals with all the possible commends """
    window = sg.Window('My To-Do App', layout)
    while True:
        event, values = window.read()
        match event:
            case 'Show':
                output = app1.show()
                window['textbox'].update(output)
            case 'Add':
                output = app1.add(values['textinput'])
                window['textbox'].update(output)
                window['textinput'].update('')
            case 'Edit':
                try:
                    # check if the number entered is a line in the to-do list
                    if app1.check_number(int(values['textinput'])):
                        # get the edited line
                        text = sg.popup_get_text('Enter The edited line', title="Waiting You Response")
                        output = app1.edit(int(values['textinput']), text)
                        # show the output
                        window['textbox'].update(output)
                        window['textinput'].update('')
                    # if the number is not valid
                    else:
                        window['textbox'].update('Invalid number, Please try again')
                # if the user didn't enter a number
                except ValueError:
                    window['textbox'].update('Please enter a number: ')
            case 'Complete':
                try:
                    output = app1.complete(int(values['textinput']))
                    window['textbox'].update(output)
                    window['textinput'].update('')
                except ValueError:
                    window['textbox'].update('Please enter a number: ')


if __name__ == '__main__':
    todo()
