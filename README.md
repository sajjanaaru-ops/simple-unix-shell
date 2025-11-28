# Simple Python Shell (PyShell)

A functional UNIX-like command-line interpreter implemented in **Python**. This project focuses on simulating the core functionalities of a standard shell environment, demonstrating key skills in command parsing, external process management, and file system interaction.

## ✨ Features Implemented

The shell currently supports essential command-line features, demonstrating core system programming and parsing skills:

* **Robust Command & Argument Parsing:** Utilizes the `shlex` module for intelligent tokenization, ensuring correct handling of arguments, especially those containing **spaces and double quotes** (e.g., `echo "Hello World"`).
* **External Command Execution:**
    * Searches directories listed in the **`$PATH`** environment variable to locate executables using custom path resolution logic.
    * Supports execution of external binaries using Python's `subprocess` module.
    * Includes logic to check for executable files and common file extensions.
* **Built-in Commands:**
    * `exit`: Terminates the shell session.
    * `echo`: Prints arguments to standard output, correctly handling quoted arguments.
    * `type`: Reports whether a command is a shell built-in or an external program, and prints its full path if external.
    * `pwd`: Prints the current working directory.
    * `cd`: Changes the current working directory, including support for the home directory (`~`) and robust error handling for non-existent paths.

## ⚙️ How to Run

### Prerequisites

* Python 3.x

### Execution

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/sajjanaaru-ops/simple-unix-shell
    cd simple-unix-shell
    ```
2.  **Run the Shell:**
    ```bash
    python app/main.py
    ```

3.  **Interact:** The shell will prompt with a `$` symbol.

    ```bash
    $ echo "This command works with spaces"
    This command works with spaces
    $ pwd
    /path/to/your/directory
    $ type ls
    ls is /bin/ls # (or equivalent path)
    $ type echo
    echo is a shell builtin
    $ exit
    ```

## 🛠️ Technical Deep Dive (app/main.py)

The core logic is built around these key Python modules and system concepts:

| Module / Concept | Purpose | Skill Demonstrated |
| :--- | :--- | :--- |
| **`shlex.split()`** | Parses the raw user input string into distinct command and argument tokens, crucial for quoting. | **Robust Parsing & Tokenization** |
| **`command_location()`** | Iterates through and searches the system's `$PATH` variable to find executables. | **Path Resolution & OS Interaction** |
| **`subprocess.run()`** | Executes external programs once their location is confirmed. | **Process Execution (High-level)** |
| **`os.chdir()` & `os.getcwd()`** | Implements the core file system navigation logic for `cd` and `pwd`. | **File System Operations** |
| **`os.environ`** | Used to access and interpret the system's environment variables, specifically `$PATH`. | **Environment Variable Handling** |
