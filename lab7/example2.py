def is_prime(num: int):
  if num < 2:
    return False
  elif num == 2:
    return True
  else:
    for n in range(2, num):
      a = (num / n)
      if float(a).is_integer():
        print(a)
        return False
    return True
