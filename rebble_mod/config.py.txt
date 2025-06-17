# config.py
import os
import json

CONFIG_DIR = os.path.expanduser("~/.rebble-mod")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

def set_rebble_path(path):
    config = load_config()
    config['rebble_path'] = path
    save_config(config)

def get_rebble_path():
    config = load_config()
    return config.get('rebble_path')
