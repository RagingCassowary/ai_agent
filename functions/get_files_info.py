import os

def get_files_info(working_directory, directory="."):
    
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    existing_dir = os.path.isdir(target_dir)
    
    if not existing_dir:
        return f'Error: "{directory}" is not a directory'
    
    dir_contents = os.listdir(target_dir)
    files = []

    for file in dir_contents:

        filepath = os.path.join(target_dir, file)
        is_dir = os.path.isdir(filepath)
        is_file = os.path.isfile(filepath)

        if not is_dir and not is_file:
            return f'Error: "{file}" is not a valid file or directory'

        file_size = os.path.getsize(filepath)

        file_data = f"- {file}: file_size={file_size} bytes, is_dir={is_dir}"

        files.append(file_data)
    
    return "\n".join(files)
        
        
