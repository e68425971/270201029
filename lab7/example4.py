import random


def get_rand_list(a: int, b: int, l: int):
    numbers = [number for number in range(min(a, b), max(a, b))]
    lastList = list()
    for i in range(0, l):
        lastList.append(random.choice(numbers))
    return (lastList)


def get_overlap():
  rangeMaker = input("""Define a and b which are our range;
And how many integers do you want in lists? define as N;
(a,b,N): """)
  rangeList = rangeMaker.split(",")

  a = get_rand_list(int(rangeList[0]), int(rangeList[1]), int(rangeList[2]))
  b = get_rand_list(int(rangeList[0]), int(rangeList[1]), int(rangeList[2]))
  print(f"Your lists are {a} and {b}")
  intersectionList =[]
  for value in a:
    if value in b:
      intersectionList.append(value)
  if len(intersectionList)>0:
    print(f"Their intersection values are {intersectionList}")
  else:
    print("There is no intersection value between them")



get_overlap()