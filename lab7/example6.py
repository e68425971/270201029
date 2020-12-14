def passwordChecker(pw: str):
    if " " in pw or len(pw) < 8:
        return 0
    else:
        securityLevel = 0
        alphabe = 0
        number = 0
        numericc = 0
        for eachValue in pw:
            if eachValue.isalpha():
                alphabe += 1
            elif eachValue.isalnum():
                number += 1
            elif eachValue.isnumeric():
                numericc += 1
        if alphabe > 1:
            securityLevel += 1
        if number > 1:
            securityLevel += 1
        if numericc > 1:
            securityLevel += 1
        return securityLevel


while True:
    password = input("Write a password: ")
    print(f"security level is {passwordChecker(password)}")