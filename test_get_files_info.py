from functions.get_files_info import get_files_info

def indent(result):
    return "\n".join("    " + line for line in result.splitlines())

print(f"Result for current directory:\n{indent(get_files_info("calculator", "."))}")

print(f"Result for 'pkg' directory:\n{indent(get_files_info("calculator", "pkg"))}")

print(f"Result for '/bin' directory:\n{indent(get_files_info("calculator", "/bin"))}")

print(f"Result for '../' directory:\n{indent(get_files_info("calculator", "../"))}")