"""
Command-line interface for Rebble modular project helper.

Supports scaffolding new projects, adding modules, and configuring settings.
"""

import argparse
import sys
import os
import json

from . import scaffold, modules

CONFIG_PATH = os.path.expanduser("~/.rebblemodconfig.json")

def load_config():
    """
    Load the CLI configuration from the config file.

    Returns:
        dict: Configuration dictionary if config file exists, else empty dict.
    """
    if os.path.isfile(CONFIG_PATH):
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_config(config):
    """
    Save the CLI configuration to the config file.

    Args:
        config (dict): Configuration dictionary to save.
    """
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

def set_rebble_path(path):
    """
    Validate and save the path to the Rebble CLI executable.

    Args:
        path (str): Path to the Rebble executable.

    Exits the program if path is invalid.
    """
    if not os.path.isfile(path) or not os.access(path, os.X_OK):
        print(f"Error: '{path}' does not exist or is not executable.")
        sys.exit(1)
    config = load_config()
    config['rebble_path'] = path
    save_config(config)
    print(f"Rebble CLI path saved: {path}")

def get_rebble_path():
    """
    Retrieve the saved Rebble CLI executable path from config.

    Returns:
        str or None: Path string if set, else None.
    """
    config = load_config()
    return config.get('rebble_path')

def main():
    """
    Parse command-line arguments and dispatch commands accordingly.
    """
    parser = argparse.ArgumentParser(description="Rebble modular project helper.")
    subparsers = parser.add_subparsers(dest='command', required=True)

    scaffold_parser = subparsers.add_parser(
        'scaffold', help='Create a new Rebble project scaffold.'
    )
    scaffold_parser.add_argument('project_name', help='Name of the new project.')
    scaffold_parser.add_argument(
        '--rebble-path', help='Path to the Rebble CLI executable.', default=None
    )

    addmod_parser = subparsers.add_parser(
        'add-module', help='Add a module to an existing project.'
    )
    addmod_parser.add_argument('project_name', help='Existing project name.')
    addmod_parser.add_argument('module_path', help='Path to the module directory or file.')

    config_parser = subparsers.add_parser('config', help='Configure settings for rebble-mod CLI.')
    config_subparsers = config_parser.add_subparsers(dest='subcommand', required=True)

    setrebble_parser = config_subparsers.add_parser(
        'set-rebble', help='Set path to Rebble CLI executable.'
    )
    setrebble_parser.add_argument('rebble_path', help='Path to Rebble executable.')

    args = parser.parse_args()

    if args.command == 'scaffold':
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
