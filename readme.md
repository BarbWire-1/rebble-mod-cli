# rebble-mod CLI Tool

`rebble-mod` is a command-line tool to scaffold and manage PebbleOS projects with modular structure.

---

## Prerequisites

- Make sure you have **Python 3.6+** installed.
- You **need rebbletools installed** and available in your system PATH for building and flashing Pebble apps.
- **Note:** Rebbletools requires **Python 2.7.x** and a compatible version of \`pip\` (usually < 20.x). This can complicate environment setup.

---

## Installation

Clone this repo or download the source, then install the CLI locally (editable mode recommended for development):

```bash
pip install -e .
```

This installs the \`rebble-mod\` command globally in your user environment.

> ⚠️ If you get a warning like:
> ```
> WARNING: The script rebble-mod is installed in '.../bin' which is not on PATH.
> ```
> Add that directory to your PATH environment variable (e.g., `export PATH="\$HOME/.local/bin:\$PATH"`).

---

## Usage

### Scaffold a new project

```bash
rebble-mod scaffold MyNewProject
```

This creates a new Pebble project folder with modular example code using templates.

---

### Add modules to an existing project

```bash
rebble-mod addModule /path/to/your/project /path/to/module
```

> TODO: Implement this feature fully.

---

## Environment setup for rebbletools

Rebbletools requires Python 2.7 and can be tricky to install alongside Python 3 environments.

### Recommended: Use a dedicated Python 2.7 virtual environment for rebbletools

\```bash
# Create and activate Python 2.7 virtualenv for rebbletools
python2.7 -m virtualenv ~/.rebbletool/venv
source ~/.rebbletool/venv/bin/activate

# Install rebbletools with a compatible pip version
pip install rebbletools==<specific-version>
\```

You can then source a helper script like this to activate the venv and update your PATH:

\```sh
#!/usr/bin/env sh
REB_VENV="\$HOME/.rebbletool/venv/bin/activate"
REB_PATH="\$HOME/.rebbletool/venv/bin"
. "\$REB_VENV"
export PATH="\$REB_PATH:\$PATH"
\```

Run it via:

\```bash
source /path/to/setup-rebble-env.sh
\```

---

## TODO

- Add detailed documentation for each CLI command.
- Implement module addition and removal commands.
- Support for rebbletools installation or environment setup from CLI.
- Add tests and CI/CD pipelines.
- Publish package to PyPI for easy installation.

---

## Contributing

Feel free to open issues or pull requests!

---

## License

[Specify your license here]
