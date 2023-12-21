import os
import shutil
import sys

# creating blank string placeholder for PATH
PATH = ''
# checking if either windows or linux platform, have not added for mac compatibility yet.
if sys.platform == "win32":
    PATH = "F:\\Ashley's Iphone Photos\\"
elif sys.platform == "linux":
    PATH = r"/home/scrant/"


# essentially moves the file to the destination, if destination does not exist, it will create the directory and store the file
def move_to_path(filename, destination) -> None:
    if not os.path.exists(destination):
        os.mkdir(destination)

    shutil.move(filename, destination)


print(sys.platform)
