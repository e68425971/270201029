numbers = "0123456789"
count = 0
Failure = -1
while count == 0:
  Failure += 1
  password = input("Write your password: ")
  if len(password) < 8:
    print("Please write at least 8 characters")
    continue
  elif password.lower() == password:
    print("Please use at least one uppercase letter")
    continue
  elif password.upper() == password:
    print("Please use at least one lowercase letter")
    continue
  if count == 0:
    for number in numbers:
      for letter in password:
        if str(letter) == str(number):
          count += 1
  if count == 0:
      print("Please use a number")

print()
if Failure > 0:
  print(f"You failed {Failure} times dude...")
  print("Next time be better")
print("It's valid man don't worry")