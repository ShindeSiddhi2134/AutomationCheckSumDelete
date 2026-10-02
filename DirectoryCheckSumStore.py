import sys
import os
import hashlib

def CalculateChecksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()
def FindDuplicate(DirectoryName):
    ret=False

    ret=os.path.exists(DirectoryName)
    if ret==False:
        print("path is invalid")
        return
    ret=os.path.isdir(DirectoryName)
    if ret==False:
        print("it is not directory")
        return
    
    
    for FolderName,SubFolder,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname=os.path.join(FolderName,fname)
            CheckSum=CalculateChecksum(fname)
            print(f"{fname}:{CheckSum}")
            if CheckSum in Duplicate:
                Same=Same+1
                Duplicate[CheckSum].append(fname)
            else:
                Unique=Unique+1
                Duplicate[CheckSum]=[fname]

        print("Unique file found:",Unique)
        print("duplicate file found:",Same)
def main():
    FindDuplicate("Test")
if __name__ == "__main__":
    main()