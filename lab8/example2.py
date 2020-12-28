def get_reversed(n):
  if len(n) == 0:
    return []
  else:
    return [n[-1]] + get_reversed(n[:-1])