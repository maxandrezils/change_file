import os           # to access the operating system
import re           # to perform a regex check on the name of the file
import shutil       # library to copy files
from os import path # access the file path i.e C:\Users\

def main(original):
    if path.exists(original):
        fileSplit = re.findall(r'\d+', original) # d+ looks for all decimals
        newDate = int(fileSplit[0]) + int(1)
        fileName = re.findall(r'(\w+ )', original)# w+space looks for all words plus spaces
        shutil.copyfile(original, ''.join(fileName)+str(newDate)+".xlsx")
        print(''.join(fileName)+str(newDate)+".xlsx" + " has been duplicated from " + original)
    else:
        print("File does not exist")


main("demo file 202002.xlsx")
