import os
import sys
import subprocess
import shutil

VENV_DIR = ".rebble_env"

def find_python27():
    import re
    candidates = ['python2.7', 'python2', '/usr/bin/python2.7', '/usr/local/bin/python2.7']
    for cmd in candidates:
        try:
            result = subprocess.run([cmd, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output = result.stdout + result.stderr
            if result.returncode == 0 and re.search(r'Python 2\.7\.\d+', output):
                return cmd
        except FileNotFoundError:
            continue
    print("Error: Python 2.7 interpreter not found on your system.")
    sys.exit(1)

def create_virtualenv(python27):
    if os.path.isdir(VENV_DIR):
        return

    print(f"Creating Python 2.7 virtual environment in ./{VENV_DIR} ...")

    try:
        subprocess.run([python27, '-m', 'virtualenv', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("Error: 'virtualenv' module not found for Python 2.7.")
        print("Please install it with: python2.7 -m pip install virtualenv")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: Python 2.7 executable not found.")
        sys.exit(1)

    try:
        subprocess.run([python27, '-m', 'virtualenv', VENV_DIR], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to create virtualenv: {e}")
        sys.exit(1)

def get_rebble_executable_from_venv():
    if os.name == "nt":
        return os.path.join(VENV_DIR, "Scripts", "rebble.exe")
    else:
        return os.path.join(VENV_DIR, "bin", "rebble")

def find_rebble():
    env_path = os.getenv("REBBLE_PATH")
    if env_path and os.path.isfile(env_path) and os.access(env_path, os.X_OK):
        return env_path

    common_paths = [
        os.path.expanduser("~/.rebbletool/rebbletool/bin/rebble"),
        "/usr/local/bin/rebble",
        "/usr/bin/rebble",
    ]
    for path in common_paths:
        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path

    path_in_path = shutil.which("rebble")
    if path_in_path:
        return path_in_path

    rebble_venv = get_rebble_executable_from_venv()
    if os.path.isfile(rebble_venv) and os.access(rebble_venv, os.X_OK):
        return rebble_venv

    return None

def run_rebble_cmd(args):
    rebble = find_rebble()
    if not rebble:
        print("Error: 'rebble' executable not found. Please install Rebble CLI or set REBBLE_PATH.")
        sys.exit(1)

    rebble_env_bin = os.path.expanduser("~/.rebbletool/.env/bin")
    rebble_is_in_env = rebble.startswith(rebble_env_bin)

    if rebble_is_in_env:
        # Run via the environment's python to ensure correct context
        python = os.path.join(rebble_env_bin, "python")
        cmd = [python, rebble] + args
    else:
        # Try direct call
        cmd = [rebble] + args

    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error running Rebble CLI:\n{result.stderr.strip()}")
        sys.exit(1)
    return result.stdout.strip()
