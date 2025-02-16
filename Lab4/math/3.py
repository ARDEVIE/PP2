from math import *

n = int(input("Input number of sides: "))
l = float(input("Input the lenght of a side: "))
apothem = l / (2 * tan(pi / n))
area = int((n * l * apothem) / 2)

print("The area of the polygon is: ", area)