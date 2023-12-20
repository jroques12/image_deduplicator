import os, shutil

win_path = r""
LIN_PATH = r"/home/scrant/"


def move_to_path(filename, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)

    shutil.move(filename, destination)
