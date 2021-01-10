def evens(x,m = 0):
    n = len(x)
    n -= 1
    if n >= 0 and x[n]%2 == 0:
        m += 1
    if n >= 0:
        evens(x[:-1],m)
    else:
        print(m)
