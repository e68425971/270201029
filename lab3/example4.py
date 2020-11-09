number = int(input("Write a number: "))
exponent = int(input("Write a exponent: "))
total = 1
for i in range(exponent):
    total *= number

print(total)