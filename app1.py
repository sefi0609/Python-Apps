import utility


def show():
    """ Returns the complete to-do ist as a string """
    prompt = ''
    todos = utility.read_from_file()
    if len(todos) != 0:
        for index, line in enumerate(todos):
            prompt += f'{index + 1}. {line.title()}'
    else:
        prompt = 'Your todo-list is empty, Please add things to do'

    return prompt


def add(todo):
    """ Add a new to-do to the list """
    todos = utility.read_from_file()
    todos.append(todo + '\n')
    utility.write_to_file(todos)
    return f'The new item: "{todo}" was added to your todo-list'


def edit(line_number, edit_line):
    """ Edit an existing line in the to-do list """
    # get the to-do list
    todos = utility.read_from_file()
    todos[line_number - 1] = edit_line + '\n'

    # write the new list to the file
    utility.write_to_file(todos)
    return f'The line number: {line_number}, has changed to "{edit_line}"'


def complete(line_number):
    """ Complete a to-do list item """
    todos = utility.read_from_file()
    # check if the number the user entered is ok
    if check_number(line_number):
        # drop the completed task
        complete_item = todos.pop(line_number - 1)

        # write the new list to the file
        utility.write_to_file(todos)
        return f'The line: "{complete_item.strip()}" has completed successfully'
    else:
        return f'Not a valid line number,\nPlease enter a number between 1 and {len(todos)}'


def check_number(line_number):
    """ Check if the number entered by the user is a valid line number in the to-do list """
    todos = utility.read_from_file()
    return utility.is_valid_number(len(todos), line_number)
