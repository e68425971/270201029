numbers1 = [2, 3, 4, 20, 5, 5, 15]
numbers2 = [10, 20, 20, 15, 30, 40]
numbers1Set = set(numbers1)
numbers2Set = set(numbers2)
intersection = set()
union = set()
for number in numbers1Set:
  for values in numbers2Set:
    if values == number:
      intersection.add(values)

for member in numbers1Set:
  union.add(member)
for member in numbers2Set:
  union.add(member)

print(union)
print(intersection)