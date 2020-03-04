import os
import shutil

def moveBasedOnName(source, destination, strCheck):
    files = os.listdir(source)
    for f in files:
        if f.startswith(strCheck):
            shutil.move(os.path.join(source, f), destination)
moveBasedOnName("new/", "demo/", "start")
