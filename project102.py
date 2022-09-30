import imp


import os
import shutil

source="C:/Users/hp/Downloads"
destination='C:/Users/hp/OneDrive/Desktop/python/Downloads'

list_files=os.listdir(source)

#print(list_files)

for file in list_files:
    files,ext=os.path.splitext(file)

    path1=source+'/'+file
    path2=destination+'/'+file

    if ext in ['.jpeg']:
        shutil.move(path1,path2)
