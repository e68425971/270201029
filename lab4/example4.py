password = input("Write a password: ")

while True:
    answer = input("Write the password: ")
    if answer == password:
        print("You are in")
        exit()
    elif answer.lower() == "help":
        print(password[0])
        continue
    elif answer == "I give up":
        exit()
    else:
        print("""YOU DON'T KNOW THE PASSWORD DUDE WHO ARE YOU""")
        continue