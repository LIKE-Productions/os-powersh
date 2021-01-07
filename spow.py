import os
import shutil
from PIL import Image


fp = os.getcwd()

class Spow:
    """
    This is the Spow class. It is a version of the OS Module made  for PowerShell like commands that take way less time and sometimes look better
    """
    
    def __init__(self):
        self.folder = "|@|"
        self.file = "/_|"

    def osn(self):
        print(os.uname())
    def spwd(self):
        print(fp)

    def sdir(self):
        print(os.listdir(fp))

    def scopy(self,source,dest):
        shutil.copy(source,dest)
    def smove(self,source,dest):
        shutil.move(source,dest)

    def skl(self):
        for folder, sub_folders, files in os.walk(fp):
            print(f"Current directory: {folder}")
            print("")
            print("The folders are:")
            for sub in sub_folders:
                print(f"{self.folder} {sub}")
            print("")
            print("The files are:")
            for f in files:
                print(f"{self.file} {f}")
            print("")
        print("End of directory")


    def sdelf(self,file):
        os.unlink(file)
    def sdeld(self,folder):
        os.rmdir(folder)
    def sdele(self,folder):
        """
        WARNING!!!! This is a very dangerous option and should not be considered!
        """
        shutil.rmtree(folder)

    
    
if __name__ == "__main__":
    spow = Spow()