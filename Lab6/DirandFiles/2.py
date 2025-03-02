import os

print('Exist:', os.access('C:/Users/DMR/Documents/PP2/Lab6/DirandFiles', os.F_OK))
print('Readable:', os.access('C:/Users/DMR/Documents/PP2/Lab6/DirandFiles', os.R_OK))
print('Writable:', os.access('C:/Users/DMR/Documents/PP2/Lab6/DirandFiles', os.W_OK))
print('Executable:', os.access('C:/Users/DMR/Documents/PP2/Lab6/DirandFiles', os.X_OK))