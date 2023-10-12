FILE_PATH = 'todo_list.txt'


def is_valid_number(number_of_lines, line_number):
    """ Check if the line number is in range """
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
