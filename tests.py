#from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

working_dir = "calculator"
# directories = ['.', 'pkg', '/bin', '../']

# for dir in directories:
#     directoryname = "current" if dir == "." else f"'{dir}'"
#     print(f"Results for {directoryname} directory:")
#     print(get_files_info(working_dir, dir))
#     print('')

# print(get_file_content("calculator", "lorem.txt"))
files = ["main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]
for file in files:
    print(get_file_content(working_dir, file))