import os
import sys
import json
import shutil

def check_path_exists(path: str, error_msg: str) -> None:
        if not os.path.exists(path):
            print(f"Error: {error_msg}")
            sys.exit(1)

def add_module(project_name, module_path):
    cwd = os.getcwd()
    project_path = os.path.join(cwd, project_name)
    modules_pool_path = os.path.join(project_path, 'modules_pool')



    check_path_exists(project_path,
                    f"Project '{project_name}' does not exist in current directory.")
    check_path_exists(modules_pool_path,
                    f"modules_pool directory does not exist in project '{project_name}'.")


    if os.path.isdir(module_path):
        c_files = [f for f in os.listdir(module_path) if f.endswith('.c')]
        h_files = [f for f in os.listdir(module_path) if f.endswith('.h')]

        if len(c_files) != 1 or len(h_files) != 1:
            print("Error: Module directory must contain exactly one .c and one .h file.")
            sys.exit(1)

        c_file = c_files[0]
        h_file = h_files[0]

        shutil.copy(os.path.join(module_path, c_file), os.path.join(modules_pool_path, c_file))
        shutil.copy(os.path.join(module_path, h_file), os.path.join(modules_pool_path, h_file))

        print(f"Copied module files {c_file}, {h_file} to modules_pool.")
    elif os.path.isfile(module_path) and (module_path.endswith('.c') or module_path.endswith('.h')):
        shutil.copy(module_path, modules_pool_path)
        print(f"Copied file {os.path.basename(module_path)} to modules_pool.")
    else:
        print("Error: module_path must be a directory containing one .c and one .h, or a single .c or .h file.")
        sys.exit(1)

    # Update modules.json if exists
    modules_json_path = os.path.join(project_path, 'modules.json')
    if os.path.isfile(modules_json_path):
        with open(modules_json_path, 'r') as f:
            data = json.load(f)
        module_name = None
        # Guess module name by the base name of c file (if added directory)
        if os.path.isdir(module_path):
            module_name = os.path.splitext(c_files[0])[0]
        else:
            module_name = os.path.splitext(os.path.basename(module_path))[0]

        if "modules" not in data:
            data["modules"] = []

        if module_name not in data["modules"]:
            data["modules"].append(module_name)
            with open(modules_json_path, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Updated modules.json with module '{module_name}'.")
