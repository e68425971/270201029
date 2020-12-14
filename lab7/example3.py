def is_prime(num: int):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for n in range(2, num):
            a = (num / n)
            if float(a).is_integer():
                print(a)
                return False
        return True


def print_primes_between(a: int, b: int):
    primeNumbers = []
    for eachValue in range(min(a, b), max(a, b)):
        if is_prime(eachValue):
            primeNumbers.append(eachValue)
    print(f"Prime numbers between {min(a, b)} and {max(a, b)}: {primeNumbers}")


print_primes_between(-3, 10)