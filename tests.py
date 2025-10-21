working_dir = "calculator"

# -------- get_files_info --------
#from functions.get_files_info import get_files_info
# directories = ['.', 'pkg', '/bin', '../']

# for dir in directories:
#     directoryname = "current" if dir == "." else f"'{dir}'"
#     print(f"Results for {directoryname} directory:")
#     print(get_files_info(working_dir, dir))
#     print('')

# -------- get_file_content --------
# from functions.get_file_content import get_file_content
# print(get_file_content("calculator", "lorem.txt"))
# files = ["main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]
# for file in files:
#     print(get_file_content(working_dir, file))

# -------- write_file --------
# from functions.write_file import write_file
# print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
# print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
# print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

from functions.run_python_file import  run_python_file
print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py"))
print(run_python_file("calculator", "nonexistent.py"))
print(run_python_file("calculator", "lorem.txt"))

