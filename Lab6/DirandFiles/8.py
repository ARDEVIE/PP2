import time
import os

if input() == '1':
  open('deleted.txt', 'w')
  print('deleted.txt was successfully opened. \n')
else:
  pass

time.sleep(4)

if os.path.exists("deleted.txt"):
  os.remove("deleted.txt")
  print("The deleted.txt file was successfully deleted.")
else:
  print("The file does not exist.")