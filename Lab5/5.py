import re

s = input()
Pattern = 'a.*?b$'
x = re.findall(Pattern, s)

if x:
    print(x)
else:
    print("None")