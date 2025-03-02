s = str(input())

upper = []
lower = []

for i in range(len(s)):
    if s[i].isupper():
        upper.append(s[i])
    else:
        lower.append(s[i])

print(len(upper), len(lower))