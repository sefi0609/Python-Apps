FILE_PATH = 'todo_list.txt'


def is_valid_number(number_of_lines):
    """ check if the line number is in range """
    while True:
        line_number = input('Please select a line number: ')
        if line_number.isnumeric() and number_of_lines >= int(line_number) >= 1:
            return int(line_number)
        else:
            print(f'Please enter a valid number from 1 to {number_of_lines}')


def write_to_file(todos, file_path=FILE_PATH):
    """ write the to-do list to a text file """
    # delete the old file
    with open(file_path, 'w') as file:
        # write the new list to the file
        file.writelines(todos)


def read_from_file(file_path=FILE_PATH):
    """ read the to-do list from a text file """
    with open(file_path, 'r') as file:
        todos = file.readlines()
    return todos
