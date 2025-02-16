def evens():
    n = int(input())
    ev = (int(i) for i in range(0, n + 1, 2))
    for i in range(int(n / 2)):
        print(next(ev), end = ", ")
    print(next(ev))

evens()