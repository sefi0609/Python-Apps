import utility
import time


def todo_list():
    """ Main function - entry point """
    # get the number of line in the to-do list
    todos = utility.read_from_file()
    number_of_lines = len(todos)

    while True:
        # start the program
        command = input('Type add, show, edit, complete or exit: ')
        command = command.strip()

        match command:
            # show the to-do list
            case 'show':
                if number_of_lines != 0:
                    todos = utility.read_from_file()
                    for index, line in enumerate(todos):
                        print(f'{index + 1}. {line.title()}', end='')
                else:
                    print('Your todo-list is empty, Please add things to do')
            # add a new to-do
            case 'add':
                while True:
                    new_line = input('To go beck to the menu press enter\nPlease add a new Task: ')
                    # an indicator to exit the add option
                    if new_line == '':
                        break

                    # add the new to-do to the list
                    number_of_lines += 1
                    todos = utility.read_from_file()
                    todos.append(new_line + '\n')
                    utility.write_to_file(todos)
                    print(f'The new item: "{new_line}" was added to your todo-list')
            # complete a to-do item
            case 'complete':
                # check if the number the user entered is ok
                line_number = utility.is_valid_number(number_of_lines)

                # drop the completed task
                todos = utility.read_from_file()
                complete = todos.pop(line_number - 1)
                number_of_lines -= 1

                # write the new list to the file
                utility.write_to_file(todos)
                print(f'The line: "{complete.strip()}" has completed successfully')
            # edit an existing to-do item
            case 'edit':
                # check if the number the user entered is ok
                line_number = utility.is_valid_number(number_of_lines)
                edit_line = input('Please Enter a new line to replace the old one: ')

                # get the to-do list
                todos = utility.read_from_file()
                todos[line_number - 1] = edit_line + '\n'

                # write the new list to the file
                utility.write_to_file(todos)
                print(f'The line number: {line_number}, has changed to "{edit_line}"')
            # exit the program
            case 'exit':
                break
            case _:
                print('Incorrect command, Please try again')

    print('Bye!')


if __name__ == '__main__':
    print(time.strftime('%B %d %Y - %H:%M:%S'))
    todo_list()
