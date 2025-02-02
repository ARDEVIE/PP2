s = str(input())
def reverse(s):
    a = s.split()
    a.reverse()
    return " ".join(a)
print(reverse(s))