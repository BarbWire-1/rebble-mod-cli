"""
Scaffold a new Rebble project with modular architecture.
Includes default modules, build scripts, and app setup.
"""

import os
import sys
import subprocess
from pathlib import Path
from .utils import find_rebble


THIS_DIR = Path(__file__).parent
TEMPLATES_DIR = THIS_DIR / 'templates'


def create_default_modules_pool(base_path):
    """
    Create modules_pool directory with example modules if missing.

    Args:
        base_path (str): Target directory path.
    """
    if not os.path.exists(base_path):
        print("modules_pool folder not found, creating default example modules...")
        os.makedirs(base_path, exist_ok=True)

        for fname in ['date_module.c', 'date_module.h', 'time_module.c', 'time_module.h']:
            src = TEMPLATES_DIR / fname
            dst = os.path.join(base_path, fname)
            with open(src, 'r', encoding='utf-8') as fsrc, open(dst, 'w', encoding='utf-8') as fdst:
                fdst.write(fsrc.read())


def write_wscript(project_path):
    """
    Write the wscript build file from template.

    Args:
        project_path (str): Project root directory.
    """
    src = TEMPLATES_DIR / 'wscript.tpl'
    dst = os.path.join(project_path, 'wscript')
    with open(src, 'r', encoding='utf-8') as fsrc, open(dst, 'w', encoding='utf-8') as fdst:
        fdst.write(fsrc.read())


def write_modules_json(project_path):
    """
    Write default modules.json manifest.

    Args:
        project_path (str): Project root directory.
    """
    modules_json_content = '''\
{
    "modules": [
        "date_module",
        "time_module"
    ]
}
'''
    with open(os.path.join(project_path, 'modules.json'), 'w', encoding='utf-8') as f:
        f.write(modules_json_content)


def overwrite_app_c(project_path, project_name):
    """
    Replace main app source with modular template.

    Args:
        project_path (str): Project root directory.
        project_name (str): Project name (source filename).
    """
    app_c_template = TEMPLATES_DIR / 'app_c.tpl'
    with open(app_c_template, 'r', encoding='utf-8') as f:
        app_c_code = f.read()
    app_c_file = os.path.join(project_path, 'src', 'c', f'{project_name}.c')
    with open(app_c_file, 'w', encoding='utf-8') as f:
        f.write(app_c_code)
    print(f"Overwritten {app_c_file} with modular app template.")


def scaffold_project(project_name, rebble_path=None):
    """
    Scaffold a new Rebble project with modular setup.

    Args:
        project_name (str): Name of the project.
        rebble_path (str, optional): Path to Rebble CLI executable.
    """
    cwd = os.getcwd()
    project_path = os.path.join(cwd, project_name)

    rebble_exe = rebble_path or find_rebble()
    if not rebble_exe:
        print("Error: 'rebble' CLI tool not found. " \
        "Please install and add to PATH or set REBBLE_PATH.")
        sys.exit(1)

    try:
        subprocess.run([rebble_exe, '--version'],
                       check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("Error: 'rebble --version' failed. Check executable.")
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
