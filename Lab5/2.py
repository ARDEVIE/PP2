import re 

str = input()
Pattern = 'a(b{2})' #^a(b*)$
Pattern2 = 'a(b{3})' #^a(b*)$

x = re.findall(Pattern, str)
x2 = re.findall(Pattern2, str)

if x2:
    print(x2)
elif x:
    print(x)
else:
    print("None")