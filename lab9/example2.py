def hailstone(x):

  if x == 1:
    return "1"
  elif x % 2 == 0:
    return str(x) + hailstone(int(x) // 2)
  else:
    return str(x)+ hailstone(3 * int(x) + 1)

