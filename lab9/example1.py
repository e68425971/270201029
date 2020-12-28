def multiplication(n):
    if n == 1:
        return 3
    else:
        return multiplication(n - 1) + 3