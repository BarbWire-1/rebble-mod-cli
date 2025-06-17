import os
import sys
import json
import subprocess
from .utils import run_rebble_cmd, find_rebble
from pathlib import Path

THIS_DIR = Path(__file__).parent
TEMPLATES_DIR = THIS_DIR / 'templates'

def create_default_modules_pool(base_path):
    if not os.path.exists(base_path):
        print("modules_pool folder not found, creating default example modules...")
        os.makedirs(base_path, exist_ok=True)

        # Copy all template module files from templates folder
        for fname in ['date_module.c', 'date_module.h', 'time_module.c', 'time_module.h']:
            src = TEMPLATES_DIR / fname
            dst = os.path.join(base_path, fname)
            with open(src, 'r') as fsrc, open(dst, 'w') as fdst:
                fdst.write(fsrc.read())

def write_wscript(project_path):
    src = TEMPLATES_DIR / 'wscript.tpl'
    dst = os.path.join(project_path, 'wscript')
    with open(src, 'r') as fsrc, open(dst, 'w') as fdst:
        fdst.write(fsrc.read())

def write_modules_json(project_path):
    modules_json_content = '''\
{
    "modules": [
        "date_module",
        "time_module"
    ]
}
'''
    with open(os.path.join(project_path, 'modules.json'), 'w') as f:
        f.write(modules_json_content)

def overwrite_app_c(project_path, project_name):
    app_c_template = TEMPLATES_DIR / 'app_c.tpl'
    with open(app_c_template, 'r') as f:
        app_c_code = f.read()
    # Replace placeholder project_name if you want; for now, just write as is
    app_c_file = os.path.join(project_path, 'src', 'c', f'{project_name}.c')
    with open(app_c_file, 'w') as f:
        f.write(app_c_code)
    print(f"Overwritten {app_c_file} with modular app template.")

def scaffold_project(project_name, rebble_path=None):
    cwd = os.getcwd()
    project_path = os.path.join(cwd, project_name)

    rebble_exe = rebble_path or find_rebble()
    if not rebble_exe:
        print("Error: 'rebble' CLI tool not found. Please install Rebble CLI, add it to PATH, or set REBBLE_PATH environment variable.")
        sys.exit(1)

    try:
        subprocess.run([rebble_exe, '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("Error: Failed to run 'rebble --version'. Is the executable valid?")
        sys.exit(1)

    print(f"Creating new rebble project '{project_name}'...")
    try:
        subprocess.run([rebble_exe, 'new-project', project_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to create rebble project: {e}")
        sys.exit(1)

    modules_pool_dst = os.path.join(project_path, 'modules_pool')

    create_default_modules_pool(modules_pool_dst)
    print(f"Copied modules_pool to {modules_pool_dst}")

    write_wscript(project_path)
    print(f"Written wscript to {project_path}/wscript")

    write_modules_json(project_path)
    print(f"Written example modules.json to {project_path}/modules.json")

    overwrite_app_c(project_path, project_name)

    print(f"Project '{project_name}' scaffolded successfully.")
