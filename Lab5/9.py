import re

s = input()
def f(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(f(s))