import re

s = input()
Pattern = '[a-z]+_[a-z]+'
x = re.findall(Pattern, s)

if x:
    print(x)
else:
    print("None")