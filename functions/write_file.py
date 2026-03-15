import os

def write_file(working_dir, filepath, content):
    
    try:
        working_dir_abs = os.path.abspath(working_dir)
        target_file = os.path.normpath(os.path.join(working_dir_abs, filepath))
        valid_filepath = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    
        if not valid_filepath:
            return f'Error: Cannot read "{filepath}" as it is outside the permitted working directory'
    
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{filepath}" as it is a directory'

        os.makedirs(os.path.dirname(target_file), exist_ok=True)
    
        with open(target_file, "w") as f:
            f.write(content)
    
        return f'Successfully wrote to "{filepath}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: could not write to file: {e}'