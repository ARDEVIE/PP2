import re 

str = input()
Pattern = '^a(b*)$'
x = re.findall(Pattern, str)

print(x)