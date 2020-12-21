def harmonic(n:int):
    if n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1)