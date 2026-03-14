import os
from config import MAX_CHARACTERS

def get_file_content(working_directory, file_path):
    
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    valid_file_path = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    
    if not valid_file_path:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    full_file_path = os.path.join(working_directory, file_path)

    if not os.path.isfile(full_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    with open(full_file_path, "r") as f:
        file_content = f.read(MAX_CHARACTERS)
        if f.read(1):
            file_content += f'[...File "{file_path}" truncated at {MAX_CHARACTERS} characters]'
    
    return file_content