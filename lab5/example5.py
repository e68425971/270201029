value = int(input("Write a value: "))
lister = []

for index in range(0, value):
  lister.append([])

counter = 0
for row in lister:
  for index in range(0, value):
    row.append(0)
  row[counter] = 1
  counter += 1

print(lister)
