import os
import shutil
import sys

# crea
PATH = ''
if sys.platform == "win32":
    PATH = "F:\\Ashley's Iphone Photos\\"
elif sys.platform == "linux":
    PATH = r"/home/scrant/"


def move_to_path(filename, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)

    shutil.move(filename, destination)


print(sys.platform)
