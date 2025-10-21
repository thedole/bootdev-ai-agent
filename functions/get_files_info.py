import os

def get_files_info(working_directory, directory="."):
    abs_workin_dir = os.path.abspath(working_directory)
    full_path = os.path.normpath(os.path.join(abs_workin_dir, directory))

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    if not full_path.startswith(abs_workin_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    
    result = []

    directory_contents = os.listdir(full_path)
    for element in directory_contents:
        file_size = os.path.getsize(os.path.join(full_path, element))
        is_directory = os.path.isdir(os.path.join(full_path, element))
        result.append(f" - {element}: file_size={file_size} bytes, is_dir={is_directory}")

    resultstring = '\n'.join(result)
    return resultstring

from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)