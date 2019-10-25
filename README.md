# vscode-tasks
This repository contains tasks for automating C and Python programming in vscode-editor.

# Table of contents
1. [Installing](#installing)
2. [Keybindings](#keybindings)
3. [Features](#features)
4. [How to use the test site?](#how-to-use-the-test-site)
5. [Test site log example](#test-site-log-example)

# Installing

### Windows
* install <b>any</b> Python <b>3.5+</b> version along with pip and <b>add it to PATH</b>
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
* On each new line, write inputs without spaces, separating them <b>";"</b> (for example: if the program accepts 3 numbers separated by spaces in one input, let these numbers be 1, 2 and 3, and the result should be 5, then you need to write <b>"1 2 3 | 5"</b>)
   * <span style="text-decoration:underline">important:</span> after the last input don't put <b>";"</b>, instead <b>";"</b> put <b>"|"</b> and write the expected outputs without spaces, separating them <b>";"</b>, after last output don't put <b>";"</b>
   * another example for program, which <b>accepts 3 names in 3 inputs and prints a greeting for them</b>, you need to write in .test file this string <b>"Pavel;Linus;Richard | Hello, Pavel, Linus, Richard!"</b>
* if you still have questions, then see the files:
    * ./test/code.c and ./test/code.c.test
    * ./test/B.py and ./test/B.py.test

# Test site log example
'''Reading /home/trvlx/Desktop/vscode-tasks/test/B.py.test
Inputs:  [['abrakadabrabrakadabra'], ['acacacaca'], ['abcabc'], ['abababab'], ['abcd'], ['tatbt'], ['abrabrab']]
Outputs:  ['YES\nabrakadabra', 'YES\nacaca', 'NO', 'YES\nababab', 'NO', 'NO', 'YES\nabrab'] 

1 test: True (expected: "YES\nabrakadabra", received: "YES\nabrakadabra", time elapsed: 0.11915707588195801)
2 test: True (expected: "YES\nacaca", received: "YES\nacaca", time elapsed: 0.03830456733703613)
3 test: True (expected: "NO", received: "NO", time elapsed: 0.021285533905029297)
4 test: True (expected: "YES\nababab", received: "YES\nababab", time elapsed: 0.0199582576751709)
5 test: True (expected: "NO", received: "NO", time elapsed: 0.020659685134887695)
6 test: True (expected: "NO", received: "NO", time elapsed: 0.01970815658569336)
7 test: True (expected: "YES\nabrab", received: "YES\nabrab", time elapsed: 0.019896268844604492)

7 of 7 tests
all-time elapsed: 0.259307861328125'''