inner = input("Write integers and split them with ' ' : ")
innerList = inner.split(" ")
print(f"Your list is {innerList}")

outerList = []

for value in innerList:
  if innerList.count(value) == 1:
    outerList.append(value)

print(outerList)