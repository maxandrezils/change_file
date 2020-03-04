import os
import re
import shutil
from os import path

def main(original):
    if path.exists(original):
        fileSplit = re.findall(r'\d+', original)
        newDate = int(fileSplit[0]) + int(1)
        fileName = re.findall(r'(\w+ )', original)
        shutil.copyfile(original, ''.join(fileName)+str(newDate)+".xlsx")
        print(''.join(fileName)+str(newDate)+".xlsx" + " has been duplicated from " + original)
    else:
        print("File does not exist")


main("guru new example 202002.xlsx")
