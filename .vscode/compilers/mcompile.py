#!/usr/bin/env python3

import os
import sys
import subprocess

# ARGS
fileDirname = sys.argv[1]

def checkCMake():
    objects = os.listdir(fileDirname)
    if "CMakeLists.txt" in objects:
        return 1
    return 0
 
if __name__ == "__main__" and checkCMake():
    cmakeFile = os.path.join(fileDirname, "CMakeLists.txt")
    subprocess.check_call(["cmake", cmakeFile], cwd=fileDirname)
    if sys.platform == "win32":
        subprocess.check_call(["cmake", "--build", "./"], cwd=fileDirname)
    else:
        subprocess.check_call(["make"], cwd=fileDirname)
else:
    print("Error: create CMakeLists.txt to compile")