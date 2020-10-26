winter = ["january","february","december"]
spring = ["march","april","may"]
summer = ["june","july","august"]
fall = ["september","october","november"]
month = input("Write a mont: ")
day = int(input("W rite a day: "))

if month.lower() == "march" and 20 > day:
  print("Season is winter")
  print(f"Your date is {month} {day}")

elif month.lower() == "june" and 21 > day:
  print("Season is spring")
  print(f"Your date is {month} {day}")

elif month.lower() == "september" and 22 > day:
  print("Season is summer")
  print(f"Your date is {month} {day}")

elif month.lower() == "december" and 21 > day:
  print("Season is fall")
  print(f"Your date is {month} {day}")

else:
  if month.lower() in spring:
    print("Season is spring")
    print(f"Your date is {month} {day}")
  elif month.lower() in summer:
    print("Season is summer")
    print(f"Your date is {month} {day}")
  elif month.lower() in winter:
    print("Season is winter")
    print(f"Your date is {month} {day}")
  elif month.lower() in fall:
    print("Season is fall")
    print(f"Your date is {month} {day}")
