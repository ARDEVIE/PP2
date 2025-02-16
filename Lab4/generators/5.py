def downto():
    n = int(input())
    decr = (int(i) for i in range (n, 0, -1))
    for i in range(n):
        print(next(decr))
        
downto()