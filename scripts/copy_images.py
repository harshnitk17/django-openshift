import pathlib
import os
from shutil import copy,rmtree

def run():
    present_path = pathlib.Path().resolve()
    present_path = str(present_path).rstrip("/hflav")
    html_path = present_path + "/b2charm/html"
    dest = str(pathlib.Path().resolve()) + "/media/images"
    try:
        rmtree(dest)
        os.mkdir(dest)
    except:
        os.mkdir(dest)

    for subdir, dirs, files in os.walk(html_path):
        for file in files:
            filename= os.path.join(subdir, file)
            if filename.endswith(".png"):
                copy(filename, dest)
