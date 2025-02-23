import re

n = input()
def camel_to_snake(text):
        str1 = re.sub('([A-Z])', r'_\1', text)
        return str1.lower()

print(camel_to_snake(n))