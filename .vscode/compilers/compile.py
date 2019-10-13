#!/usr/bin/env python3

import os
import sys
import subprocess

# ARGS
fileDirname = sys.argv[1]
fileBasename = sys.argv[2]
workspaceFolder = sys.argv[3]

# TRANSFORMATION
filepath = os.path.join(fileDirname, fileBasename)
fileBasenameNewExtension = ".exe".join(fileBasename.rsplit(".c", 1))
relativeFileDirname = fileDirname[len(workspaceFolder)+1:]
distpath = os.path.join(workspaceFolder, "cdist", relativeFileDirname, fileBasenameNewExtension)
relativeFileDirname = os.path.join("cdist", relativeFileDirname)

# COMMAND GENERATOR
def construct():
    COMMAND = []
    if sys.platform == "win32":
        COMMAND.append("g++")
    else:
        COMMAND.append("gcc")
    COMMAND.append(filepath)
    COMMAND.append("-o")
    COMMAND.append(distpath)

    return COMMAND

# CREATES ALL DIRS IN PATH
def create_dirs():
    folders = []
    path = relativeFileDirname
    while True:
        path, folder = os.path.split(path)
        if folder != "":
            folders.append(folder)
        else:
            break
    folders.reverse()

    if folders == []:
        path = os.path.join(workspaceFolder, "cdist")
        if not os.path.isdir(path):
            os.mkdir(path)
    else:
        path = workspaceFolder
        for folder in folders:
            path = os.path.join(path, folder)
            if not os.path.isdir(path):
                os.mkdir(path)

if __name__ == "__main__":
    COMMAND = construct()
    create_dirs()
    subprocess.check_call(COMMAND, cwd=fileDirname)  ## cwd - cd current path