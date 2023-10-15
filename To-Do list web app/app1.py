import os

FILE_PATH = 'todo_list.txt'
INDICATOR = False


def add(todo):
    """ Add a new to-do to the list """
    todos = read_from_file()
    # make sure this is not an existing line from the to-do list
    if not todo.endswith('\n'):
        todo = todo.title() + '\n'

    if todo not in todos:
        todos.append(todo)
        write_to_file(todos)
    else:
        return f'This todo: "{todo.strip()}" is already in your list'


def edit(old_line, new_line):
    """ Edit an existing line in the to-do list """
    # get the to-do list
    todos = read_from_file()
    # make sure this is not an existing line from the to-do list
    if not new_line.endswith('\n'):
        new_line = new_line.title() + '\n'

    if new_line not in todos:
        index = todos.index(old_line)
        todos[index] = new_line
        # write the new list to the file
        write_to_file(todos)
    else:
        return f'This todo: "{new_line.strip()}" is already in your list'


def complete(todo):
    """ Complete a to-do list item """
    todos = read_from_file()
    # drop the completed task
    todos.remove(todo)
    # write the new list to the file
    write_to_file(todos)


def write_to_file(todos, file_path=FILE_PATH):
    """ Write the to-do list to a text file """
    # delete the old file
    with open(file_path, 'w') as file:
        # write the new list to the file
        file.writelines(todos)


def read_from_file(file_path=FILE_PATH):
    """ Read the to-do list from a text file """
    with open(file_path, 'r') as file:
        # read lines as a list
        todos = file.readlines()
    return todos


def file_exists():
    """ Check if the to-do list fill exists, if not create it """
    if not os.path.isfile(FILE_PATH):
        with open(FILE_PATH, 'w') as f:
            pass


# make sure the to-do file exists before continuing the program
file_exists()
