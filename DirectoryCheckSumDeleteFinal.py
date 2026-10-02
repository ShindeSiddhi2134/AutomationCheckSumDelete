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
            
            if CheckSum in Duplicate:
                Same=Same+1
                Duplicate[CheckSum].append(fname)
            else:
                Unique=Unique+1
                Duplicate[CheckSum]=[fname]

        return Duplicate
def DeleteDuplicate(DirectoryName):
    Mydict=FindDuplicate(DirectoryName)
    
    Result=list(filter(lambda x:len(x)>1,Mydict.values()))
    Count =0
    TotalDeleted=0
    for values in Result:
        
        for Subvalue in value:

            Count=Count+1
            if(Count>1):
                os.remove(Subvalue)
                
                TotalDeleted=TotalDeleted+1
            
        Count=0
    print("total deleted files;",TotalDeleted)
    
def main():

    data=DeleteDuplicate("Test")
    print(data)
if __name__ == "__main__":
    main()