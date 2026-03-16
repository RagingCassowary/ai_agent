import os
import subprocess

def run_python_file(working_dir, filepath, args=None):
    try:
        working_dir_abs = os.path.abspath(working_dir)
        target_file = os.path.normpath(os.path.join(working_dir_abs, filepath))
        valid_filepath = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    
        if not valid_filepath:
            return f'Error: Cannot execute "{filepath}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{filepath}" does not exist or is not a regular file'
        
        if filepath[-3:] != ".py":
            return f'Error: "{filepath}" is not a Python file'
        
        command = ["python", target_file]

        if args != None:
            command.extend(args)
        
        completed_process = subprocess.run(command, capture_output=True, text=True, timeout=30, cwd=working_dir_abs)

        output = []
        return_code = completed_process.returncode
        stdout = completed_process.stdout
        stderr = completed_process.stderr

        if return_code != 0:
            output.append(f"Process exited with code {return_code}")
        
        if stdout == "" and stderr == "":
            output.append("No output produced")
        
        if stdout != "":
            output.append(f"STDOUT: {stdout}")
        
        if stderr != "":
            output.append(f"STDERR: {stderr}")
        
        return " ".join(output)
    
    except Exception as e:
        return f"Error: could not execute Python file: {e}"
        


