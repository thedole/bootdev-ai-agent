import os
from functions.config import MAX_CHARS
def get_file_content(working_directory, file_path):
    abs_workin_dir = os.path.abspath(working_directory)
    full_path = os.path.normpath(os.path.join(abs_workin_dir, file_path))

    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    if not full_path.startswith(abs_workin_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    file_content_string = ""
    try:
        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            file_pos = f.tell()
            f.seek(0, os.SEEK_END)
            end_pos = f.tell()
            if file_pos < end_pos:
                file_content_string += f'\n[...File "{file_path}" truncated at 10000 characters]'
    except Exception as e:
        return f'Error: Processing file "{file_path}" failed.'

    return file_content_string