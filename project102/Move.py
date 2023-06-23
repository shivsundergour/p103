import os
import shutil
source="C:/Users/hp/Downloads"
dest="C:/Users/hp/Desktop/document files"
listOfFiles=os.listdir(source)
print(listOfFiles)
for fileName in listOfFiles:
    name,extension=os.path.splitext(fileName)
    print(name,extension)
    if extension =='':
        continue
    if extension in [".txt", ".doc", ".docx", ".pdf"]:
        path1=source+"/"+fileName
        path2=dest+"/"+'Document_Files'
        path3=dest+"/"+'Document_Files'+"/"+fileName 
        print("Path1",path1)
        print("Path3",path3)
        if os.path.exists(path2):
            print("moving...."+fileName)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving...."+fileName)
            shutil.move(path1,path3)