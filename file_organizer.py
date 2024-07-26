import os
from pathlib import Path
import shutil

os.chdir("/home/jannatulf/Downloads/")

for file in os.listdir():
    if os.path.isfile(file):
        extension = Path(file).suffix[1:]
        destination = os.path.join("/home/jannatulf/Downloads/", extension)
        if not os.path.exists(destination):
            os.mkdir(destination)
        shutil.move(file, os.path.join(destination, file))

    