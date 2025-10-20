from functions.get_files_info import get_files_info

working_dir = "calculator"
directories = ['.', 'pkg', '/bin', '../']

for dir in directories:
    directoryname = "current" if dir == "." else f"'{dir}'"
    print(f"Results for {directoryname} directory:")
    print(get_files_info(working_dir, dir))
    print('')