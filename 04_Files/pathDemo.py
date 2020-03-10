import os.path
import sys
startPath = r'C:\Kevin\proj\python_training'
print(__file__)

# add a directory to the path:
path2Lesson1Dir = os.path.join(startPath, '01_ToolOrientation')
print(f"path2Lesson1Dir {path2Lesson1Dir}")


# does the directory exist
if os.path.exists(path2Lesson1Dir):
    print(f'path2Lesson1Dir: {path2Lesson1Dir} exists')
else:
    print(f'path2Lesson1Dir: {path2Lesson1Dir} DOES NOT exist')



# Create this path to a file
# C:\Kevin\proj\python_training\01_ToolOrientation\hello.py
helloPyPath = os.path.join(startPath, '01_ToolOrientation','hello.py')
print(f"helloPyPath: {helloPyPath}")



# get just hello.py from the path
justHelloPy = os.path.basename(helloPyPath)
print(f"just the hello.py file: {justHelloPy}")

# just the directory that from the fullpath to hello.py
helloDir = os.path.dirname(helloPyPath)
print(f'the enclosing directory for hello.py file is: {helloDir}')

# doing the same thing in one line
helloDir, justHelloPy = os.path.split(helloPyPath)
aList = os.path.split(helloPyPath)
print(f'returned: {aList}, {type(aList)}')
print(f"hello dir: {helloDir}")
print(f"hello file: {justHelloPy}")
