import os

def write_file(working_directory, file_path, content):
    abs_workin_dir = os.path.abspath(working_directory)
    full_path = os.path.normpath(os.path.join(abs_workin_dir, file_path))

    if not full_path.startswith(abs_workin_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    try:
        directory_name = os.path.dirname(full_path)
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
    except Exception as e:
        return f"Error: can't create directory {directory_name}"
    
    try:
        f = open(full_path, 'w')
    except FileNotFoundError:
        return f"Error: can't open file {full_path}"
    else:
        with f:
            f.write(content)
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'