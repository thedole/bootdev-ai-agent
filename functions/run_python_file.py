import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    full_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

    if not full_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    command = ["python3", file_path] + args
    try:
        completed_process = subprocess.run(command, cwd=abs_working_dir, timeout=30, capture_output=True)
    except Exception as e:
        return f"Error: executing Python file: {e}"

    if not completed_process.stdout and not completed_process.stderr:
        return "No output produced"
    
    return f"STDOUT: {completed_process.stdout}\n\nSTDERR: {completed_process.stderr}"