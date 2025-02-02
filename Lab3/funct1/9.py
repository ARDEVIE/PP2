import math 
r = float(input())
def volume(r):
    v = (4/3) * math.pi * (r ** 3)
    return v

print(volume(r))