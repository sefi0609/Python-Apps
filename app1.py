FILE_PATH = 'todo_list.txt'


def add(todo):
    """ Add a new to-do to the list """
    todos = read_from_file()
    todos.append(todo + '\n')
    write_to_file(todos)
    return f'The new item: "{todo}" was added to your todo-list'


def edit(old_line, new_line):
    """ Edit an existing line in the to-do list """
    # get the to-do list
    todos = read_from_file()
    todos[line_number - 1] = edit_line + '\n'

    # write the new list to the file
    write_to_file(todos)
    return f'The line number: {line_number}, has changed to "{edit_line}"'


def complete(todo):
    """ Complete a to-do list item """
    todos = read_from_file()
    # drop the completed task
    todos.remove(todo)
    # write the new list to the file
    write_to_file(todos)
    return f'The line: "{todo.strip()}" has completed successfully'


def is_valid_number(line_number):
    """ Check if the number entered by the user is a valid line number in the to-do list """
    todos = read_from_file()
    number_of_lines = len(todos)
    while True:
        if number_of_lines >= line_number >= 1:
            return True
        else:
            return False


def write_to_file(todos, file_path=FILE_PATH):
    """ Write the to-do list to a text file """
    # delete the old file
    with open(file_path, 'w') as file:
        # write the new list to the file
        file.writelines(todos)


def read_from_file(file_path=FILE_PATH):
    """ Read the to-do list from a text file """
    with open(file_path, 'r') as file:
        todos = file.readlines()
    return todos
