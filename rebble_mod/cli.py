import argparse
import sys
import os
import json

from . import scaffold, modules

CONFIG_PATH = os.path.expanduser("~/.rebblemodconfig.json")

def load_config():
    if os.path.isfile(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    return {}

def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)

def set_rebble_path(path):
    if not os.path.isfile(path) or not os.access(path, os.X_OK):
        print(f"Error: '{path}' does not exist or is not executable.")
        sys.exit(1)
    config = load_config()
    config['rebble_path'] = path
    save_config(config)
    print(f"Rebble CLI path saved: {path}")

def get_rebble_path():
    config = load_config()
    return config.get('rebble_path')

def main():
    parser = argparse.ArgumentParser(description="Rebble modular project helper.")
    subparsers = parser.add_subparsers(dest='command', required=True)

    scaffold_parser = subparsers.add_parser('scaffold', help='Create a new rebble project scaffold.')
    scaffold_parser.add_argument('project_name', help='Name of the new project.')
    scaffold_parser.add_argument('--rebble-path', help='Path to the rebble CLI executable.', default=None)

    addmod_parser = subparsers.add_parser('add-module', help='Add a module to an existing project.')
    addmod_parser.add_argument('project_name', help='Existing project name.')
    addmod_parser.add_argument('module_path', help='Path to the module directory or file.')

    config_parser = subparsers.add_parser('config', help='Configure settings for rebble-mod CLI.')
    config_subparsers = config_parser.add_subparsers(dest='subcommand', required=True)

    setrebble_parser = config_subparsers.add_parser('set-rebble', help='Set path to rebble CLI executable.')
    setrebble_parser.add_argument('rebble_path', help='Path to rebble executable.')

    args = parser.parse_args()

    if args.command == 'scaffold':
        # Use --rebble-path if given, else fallback to config file path
        rebble_path = args.rebble_path or get_rebble_path()
        scaffold.scaffold_project(args.project_name, rebble_path)
    elif args.command == 'add-module':
        modules.add_module(args.project_name, args.module_path)
    elif args.command == 'config':
        if args.subcommand == 'set-rebble':
            set_rebble_path(args.rebble_path)
        else:
            print("Unknown config subcommand")
            sys.exit(1)
    else:
        print("Unknown command")
        sys.exit(1)

if __name__ == "__main__":
    main()
