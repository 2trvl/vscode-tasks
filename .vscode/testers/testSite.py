#!/usr/bin/env python3

import os
import sys
import subprocess

scriptPath = sys.argv[1]
testFilePath = sys.argv[2]
scriptExtension = sys.argv[3]
fileDirname = sys.argv[4]
workspaceFolder = sys.argv[5]
fileBasename = sys.argv[6]
inputs = []
outputs = []

def read_test_file():
    for line in open(testFilePath).readlines():
        # split input and output lines
        line = line.split("|")
        # split inputs
        line[0] = line[0].strip()
        line[0] = line[0].split(";")
        inputs.append(line[0])
        # append output in list
        line[1] = line[1].strip()
        outputs.append(line[1])

def get_compiled_clang_path():
    fileBasenameNewExtension = ".exe".join(fileBasename.rsplit(".c", 1))
    relativeFileDirname = fileDirname[len(workspaceFolder)+1:]
    compiledClang = os.path.join(workspaceFolder, "cdist", relativeFileDirname, fileBasenameNewExtension)
    return compiledClang

if __name__ == "__main__":
    # read test file and print info
    print("Reading %s" % testFilePath)
    try:
        read_test_file()
    except FileNotFoundError:
        print("Warning: Сreate test file with name <YourFileBasename>.test")
    print("Inputs: ", inputs)
    print("Outputs: ", outputs)

    # run tests
    if scriptExtension == ".py":
        for index, task in enumerate(inputs):
            process = subprocess.Popen([sys.executable, scriptPath], stdout=subprocess.PIPE, 
                                       stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
            task = ("\n".join(task) + "\n").encode()
            taskOutput = process.communicate(input=task)[0].decode().strip()
            # print results
            print("%s test: %s (expected: %s, received: %s)" % (index+1, taskOutput==outputs[index], outputs[index], taskOutput))
    
    elif scriptExtension == ".c":
        compiledClang = get_compiled_clang_path()
        print("Running %s" % compiledClang)
        
        if os.path.isfile(compiledClang):
            for index, task in enumerate(inputs):
                process = subprocess.Popen([compiledClang], stdout=subprocess.PIPE, 
                                           stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
                task = ("\n".join(task) + "\n").encode()
                taskOutput = process.communicate(input=task)[0].decode().strip()
                # print results
                print("%s test: %s (expected: %s, received: %s)" % (index+1, taskOutput==outputs[index], outputs[index], taskOutput))
        else:
            print("Warning: Compile clang before test it")
    
    else:
        print("Warning: Only .c and .py extensions supported by this task")