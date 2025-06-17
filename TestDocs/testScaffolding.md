
## Installing the CLI script
This section shows how to install the CLI tool in editable/development mode using pip install -e .. This allows you to make changes to the source code and have them immediately reflected without reinstalling the package.

💡 This is especially useful when you're actively developing or debugging the CLI.

Note that the example below also includes typical macOS shell environment messages (e.g., switching from Bash to Zsh).

After installation, you can test the CLI by running the project scaffolding command inside the rebble-mod-cli directory, with the Python virtual environment activated.

```bash
bash: /Users/barbara/.profile: No such file or directory

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
iMac-von-Barbara:rebble-mod-cli barbara$ pip install -e

Usage:
  pip install [options] <requirement specifier> [package-index-options] ...
  pip install [options] -r <requirements file> [package-index-options] ...
  pip install [options] [-e] <vcs project url> ...
  pip install [options] [-e] <local project path> ...
  pip install [options] <archive url/path> ...

-e option requires 1 argument
```
> ### Manual test for project scaffolding
>Run this inside the rebble-mod-cli directory with the Python virtual environment activated to create the example directly in the project folder.
>
>Alternatively, if you've installed the CLI via pip install -e ., you can run the command from anywhere, as long as the virtual environment is active.

```bash
 $ rebble-mod scaffold MyNewProject
 iMac-von-Barbara:rebble-mod-cli barbara$ source ~/.zshrc
```
### Output
```zsh
(.env) iMac-von-Barbara:rebble-mod-cli barbara$ rebble-mod scaffold MyNewProject
Creating new rebble project 'MyNewProject'...
Created new project MyNewProject
modules_pool folder not found, creating default example modules...
Copied modules_pool to /Users/barbara/Desktop/rebble-mod-cli/MyNewProject/modules_pool
Written wscript to /Users/barbara/Desktop/rebble-mod-cli/MyNewProject/wscript
Written example modules.json to /Users/barbara/Desktop/rebble-mod-cli/MyNewProject/modules.json
Overwritten /Users/barbara/Desktop/rebble-mod-cli/MyNewProject/src/c/MyNewProject.c with modular app template.
Project 'MyNewProject' scaffolded successfully.
(.env) iMac-von-Barbara:rebble-mod-cli barbara$
```
