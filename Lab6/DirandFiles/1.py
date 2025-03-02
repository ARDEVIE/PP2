import os

path = "C:/Users/DMR/Documents/PP2/Lab6/DirandFiles"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
for i in dir_list:
    print(i, end="\n")
    