
# ⚠️ Experimental Work In Progress ⚠️
## rebble-mod CLI Tool


Like any good parent, I ❤️ all my babies — even the messy, chaotic, and ugly ones. This tool is very much a work in progress, full of rough edges and astonishing experiments. 🍼✨

### 📁 Quick start

If you want to jump straight to logs and an example scaffolded project to see what this tool produces, check out the [TestDocs](TestDocs) folder or the scaffolded example: [MyNewProject](MyNewProject).


---
### 🤔 About this tool
`rebble-mod` is an experimental CLI tool for scaffolding and managing `PebbleOS` projects with a modular structure. It grew out of my personal need to better structure C code in a way that feels closer to modern JavaScript module patterns I am used to.

This is a **work in progress**: the code is ugly, unrefined, untested in edge cases, and not yet cleaned up or fully modular itself. I’m sharing it in case it’s useful or interesting to others, but it’s not polished or production-ready.
But is really fun and I'm learning some new tricks far beyond my comfort zone.

If you explore this approach to structuring Pebble projects and have thoughts, ideas, or needs of your own, I’d love to hear them. Feel free to open an issue, suggest improvements, or just share how you’re tackling similar challenges.

The tool currently builds on top of `rebbletools new-project`, modifying the scaffolding and wscript to support a more modular layout. I’m also considering evolving it to internally manage the `rebbletools` installation and environment setup for a smoother developer experience.

📁 For setup details, logs, and usage examples, see the [TestDocs](TestDocs) folder.

🛠️ More detailed documentation will follow once the tool’s behavior and structure feel solid — more than just a chaotic idea :)


___

#### Prerequisites

<details>
  	<summary>Show details</summary>

- Make sure you have **Python 3.6+** installed.
- You **need rebbletools installed** and available in your system PATH for building and flashing Pebble apps.
- **Note:** Rebbletools requires **Python 2.7.x** and a compatible version of \`pip\` (usually < 20.x). This can complicate environment setup.

> ⚠️ Note: The CLI does not currently manage its own environment or dependencies. You’ll need to set up and activate the required environment manually.
</details>

#### Installation
<details>
  	<summary>Show Details</summary>



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
</details>


#### Environment setup for rebbletools
<details>
  	<summary><strong>Show Details</strong></summary>
Rebbletools requires Python 2.7 and can be tricky to install alongside Python 3 environments.

### Recommended: Use a dedicated Python 2.7 virtual environment for rebbletools

```bash
# Create and activate Python 2.7 virtualenv for rebbletools
python2.7 -m virtualenv ~/.rebbletool/venv
source ~/.rebbletool/venv/bin/activate

# Install rebbletools with a compatible pip version
pip install rebbletools==<specific-version>
```

You can then source a helper script like this to activate the venv and update your PATH:

```sh
#!/usr/bin/env sh
REB_VENV="$HOME/.rebbletool/venv/bin/activate"
REB_PATH="$HOME/.rebbletool/venv/bin"
. "$REB_VENV"
export PATH="$REB_PATH:$PATH"
```

Run it via:

```bash
source /path/to/setup-rebble-env.sh
```
</details>

---
### Usage

#### Scaffold a new project

```bash
rebble-mod scaffold MyNewProject
```

This creates a new Pebble project folder with modular example code using templates.


#### Add modules to an existing project

```bash
rebble-mod addModule /path/to/your/project /path/to/module
```

> TODO: Implement this feature fully - not tested in this version.
</details>

---



#### TODOs

- Add detailed documentation for each CLI command.
- Implement module addition and removal commands.
- Support for rebbletools installation or environment setup from CLI.
- Add tests and CI/CD pipelines.
- Publish package to PyPI for easy installation.
- ...
---

### Contributing

Feel free to open issues or pull requests!

---

#### License

This project is licensed under the [MIT License](LICENSE).
