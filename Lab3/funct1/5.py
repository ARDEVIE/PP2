import math
from itertools import permutations

str1 = str(input())

def permutation(str1):
    a = len(str1)
    for i in permutations(str1):
        b = ''
        for j in i:
            b += str(j)
        print(b)
    return math.factorial(a)

print(permutation(str1))