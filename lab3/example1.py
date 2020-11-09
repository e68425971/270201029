number = input("Write an integer value: ")

result = 0

if len(number) >= 2:
    result = + int(number[-1]) + int(number[-2])
    print(result)
else:
    print("0" + number[-1])