price = 3
age = float(input("write you age: "))

if 6 > age or age > 60:
  print("you are free, Next")

elif 18 > age > 6:
  price= price / 2
  print(f"discount price is {price}tl")

else:
  print("Price is usual price 3 tl")