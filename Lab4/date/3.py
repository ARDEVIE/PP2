import datetime

today = datetime.datetime.now()
print(today) 
today = str(today)
woutmicro = today.split(".")
print(woutmicro[0])