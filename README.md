# vscode-tasks
This repository contains tasks for automating C and Python programming in vscode-editor.

# Table of contents
1. [Installing](#installing)
2. [Keybindings](#keybindings)
3. [Features](#features)
4. [How to use the test site?](#how-to-use-the-test-site)

# Installing

### Windows
* install <b>any</b> Python <b>3.5+</b> version with pip and <b>add it to PATH</b>
* install MinGW compiler and <b>add it to PATH</b>
* with vscode open press <b>[ctrl+shift+p]</b>
    * print <i>"Preferences: Open Keyboard Shortcuts (JSON)"</i> and press [enter], copy to the opened file all strings from <i>.vscode/keybindings.json</i>
* with your terminal open as administrator run this commands:
    * <b>python -m pip install --upgrade pip</b>
    * <b>pip install pyinstaller</b>

### Linux
* with vscode open press <b>[ctrl+shift+p]</b>
    * print <i>"Preferences: Open Keyboard Shortcuts (JSON)"</i> and press <b>[enter]</b>, copy to the opened file all strings from .vscode/keybindings.json
* with your terminal open
    * install package named <i>"pyinstaller"</i> through python 3 pip (for example <b>in ArchLinux:</b> <i>"sudo pip install pyinstaller"</i>, <b>in Ubuntu:</b> <i>"sudo apt install python3-pip; sudo pip3 install pyinstaller"</i>)

# Keybindings

* <b>[f2]</b> - show build tasks
* <b>[f3]</b> - show run tasks
* <b>[numpad2]</b> - focus on the integrated terminal
* <b>[numpad8]</b> - focus on the code area

<b>important:</b> to use numpad2 and numpad8 disable num lock

# Features

* Compile
    * clang (placed in <i>./cdist</i>)
    * python in one .exe (via pyinstaller, placed in <i>./pydist</i>)
* Run
    * compiled clang
    * python code <i><span style="text-decoration:underline">(through the interpreter)</span></i>
* Test
    * clang
    * python code

# How to use the test site?

* Сreate test file with name <<i>YourFileBasename</i>><i>.test</i>
    * for example: code.c --> code.c.test, where <b>code.c.test is a file with tests for code.c</b>
* On each new line, write inputs without spaces, separating them <i>";"</i> (for example: if the program accepts 3 numbers without spaces in one input, let these numbers be 1, 2 and 3, and the result should be 5, then you need to write "1 2 3 | 5")
   * <span style="text-decoration:underline">important:</span> after the last input do not put ";", instead ";" put "|" and write the expected output
   * another example for program, which <b>accepts 3 names and prints a greeting for them</b>, you need to write in .test file this string "Pavel;Linus;Richard | Hello, Pavel, Linus, Richard!"
* if you still have questions, then see the files:
    * ./test/code.c and ./test/code.c.test
    * ./test/code.py and ./test/code.py.test
