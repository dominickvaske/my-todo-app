def get_todos(filepath='todos.txt'):
    """
    Read a text file and return list of todo items
    :param filepath: string of file path to read from
    :return: todos_local: list of todo items from filepath
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath='todos.txt'):
    """
    Write a list of todo items to the provided file path
    :param todos_arg: List of todo items to write
    :param filepath: path of file to write to
    :return: None
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
