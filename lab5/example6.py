value = int(input("Write a value: "))
lister = []

for index in range(0, value):
  row = input(f"write {value} integers and split with space: ")
  rower = row.split()
  lister.append(rower)

for printer in lister:
  print(printer)

count = 0
total = 0
for sub in range(0, value):
  total += int(lister[sub][sub])

print(total)
