number1 = (input("Write an positive integer: "))
number2 = (input("Write an positive integer: "))
matchNumber = 0

while number1 > 0 and number2 > 0:
    if number1 % 10 == number2 % 10:
        matchNumber += 1
    number1 //= 10
    number2 //= 10

print(matchNumber)