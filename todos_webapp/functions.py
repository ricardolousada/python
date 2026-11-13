FILE_PATH = "todos.txt"

def get_todos(filepath=FILE_PATH):
    """Read todos.txt file and return a list of the todos"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath=FILE_PATH):
    """Write todos.txt file with the new todos"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)