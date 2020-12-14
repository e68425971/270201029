process = input("""1)Binary to hexadecimal
2)Hexadecimal to binary
What do you want? (1 / 2) """)


def binary_to_dec():
    lastHexadecimal = 0
    binaryText = input("\nBinary value: ")
    binaryText = binaryText[::-1]
    for i in range(0, len(binaryText)):
        lastHexadecimal += (2 ** i) * (int(binaryText[i]))
    print(f"Hexadecimal representation is {lastHexadecimal}")


def dec_to_binary():
    lastBinary = ""
    hexadecimalText = input("\nHexadecimal value: ")
    while int(hexadecimalText) > 0:
        addBinary = int(hexadecimalText) % 2
        lastBinary += str(addBinary)
        hexadecimalText = (int(hexadecimalText) / 2) // 1
    print(f"Binary representation is {lastBinary}")


if process == "1":
    binary_to_dec()

elif process == "2":
    dec_to_binary()