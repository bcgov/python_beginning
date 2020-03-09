import os
# create a directory path
newDir = os.path.join('.', 'junkdir')
newDir = os.path.abspath(newDir)
print(f'full path to dir to create: {newDir}')
if not os.path.exists(newDir):
    os.mkdir(newDir)
    print(f"created single dir: {newDir}")

# add a bunch more paths to newDir
newDirSubPaths = os.path.join(newDir, 'somedir', 'anotherdir', 'andAnother')
if not os.path.exists(newDirSubPaths):
    os.makedirs(newDirSubPaths)
    print(f"created a bunch of sub dirs..: {newDirSubPaths}")

# create an empty file
subDirWithFile = os.path.join(newDirSubPaths, 'somefile.txt')
with open(subDirWithFile, 'w') as fh:
    fh.write("add one line to the file\n")
    print(f'created the file: {subDirWithFile}')

# use os.remove to delete the file
if os.path.exists(subDirWithFile):
    os.remove(subDirWithFile)
    print(f"delete the file: {subDirWithFile}")

# delete the dir andAnother
if os.path.exists(newDirSubPaths):
    os.rmdir(newDirSubPaths)
    print(f"deleted the directory: {newDirSubPaths}")

# delete all the dirs:
if os.path.exists(newDir):
    os.rmdir(newDir)
    print(f"deleted the dir and subdirs {newDir}")
    # ERROR!