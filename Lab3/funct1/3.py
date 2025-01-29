def solve(numheads, numlegs):
    chicken = 0
    rabbit = 0
    rabbit = (numlegs - 2 * numheads) / 2
    chicken = numheads - rabbit 
    return int(chicken), int(rabbit)

print(solve(int(input()), int(input())))