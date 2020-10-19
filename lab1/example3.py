print('ı can solve a equation in addition it has to be like "ax**2+bx+c= 0"')
a = float(input('write an "a" '))
b = float(input('write a "b" '))
c = float(input('write a "c" '))

delta = b * b - (4 * a * c)
print(f"Delta is {delta} and then:")

if delta > 0:
    print('There are two term for x:')
    x1 = ((-b) + (float(delta) ** (1 / 2))) / (2 * a)
    print(f"First term is; {x1}")
    x2 = ((-b) - (float(delta) ** (1 / 2))) / (2 * a)
    print(f"Second term is; {x2}")

elif delta == 0:
    print('There are only one term for x:')
    x1 = ((-b) + (float(delta) ** (1 / 2))) / (2 * a)
    print(f"Term is; {x1}")

elif delta < 0:
    print('There are no real term.')
