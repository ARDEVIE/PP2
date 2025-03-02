import math

list1 = []
n = int(input())

for i in range(n):
    i = int(input())
    list1.append(i)

result1 = math.prod(list1)

print(result1)