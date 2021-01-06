import os
import shutil
from PIL import Image


file_path = os.getcwd()
folder = Image.open("./Images/Folder Icon.tif");
file = Image.open("./Images/File Icon.tif");

class Spow:
    
    
    def __init__(self):
        pass

    def spwd(self):
        print(file_path)

    def sdir(self):
        for folder, sub_folders, files in os.walk(file_path):
            print(f"Currently looking at {folder}")
            print("\n")

            for sub_fold in sub_folders:  
                print(f"\t Subfolder: {sub_fold}")
            print("The files are:")
            for f in files:
                print(f"\t File: {f}")
            print("\n")
        print("End of directory.")

    def scopy(self):
         source = input("What is your source file or folder?\n")

spow = Spow()
spow.spwd()
spow.sdir()
