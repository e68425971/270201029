dict = {}
counter = 0
books = ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", "ENDER'S GAME"]
listTuple = []
for book in books:
  first = len(book)
  for letter in book:
    if book.count(letter) == 1:
      counter += 1
      second = counter
  listTuple.append((first, second))
print(books)
print(listTuple)
for i in range(0, len(books)):
  dict.update({books[i]: listTuple[i]})
for indexs in dict:
  print(f"{indexs} -> {dict[indexs]}")