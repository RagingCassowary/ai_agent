import os

def write_file(working_dir, filepath, content):
    
    try:
        working_dir_abs = os.path.abspath(working_dir)
        target_file = os.path.normpath(os.path.join(working_dir_abs, filepath))
        valid_filepath = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    except:
        return f'Error: Could not validate filepath to "{filepath}"'
    
    if not valid_filepath:
        return f'Error: Cannot read "{filepath}" as it is outside the permitted working directory'
    
    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{filepath}" as it is a directory'

    try: 
        full_filepath = os.path.join(working_dir, filepath)
        os.makedirs(full_filepath, exist_ok=True)
    except:
        return f'Error: Could not construct full filepath to "{filepath}"'


    with open(full_filepath, "w") as f:
        f.write(content)
    
    return f'Successfully wrote to "{filepath}" ({len(content)} characters written)'
