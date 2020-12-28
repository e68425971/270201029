"""Burada 'memorization'dan bahsedeceğiz. Memorization bazı tekniklerle hafızayı manüpüle etmektir.
Buradaki recursionı yormamak adına eğer daha önceden o değer hesaplandıysa onu bir sözlüğe atıp
gerektiğinde onu sözlükten çekip hesaplamayı tekrarlamaya gerek kalmdan dönebilmektir"""

fiboCache = {}

def fib(n):
  if n in fiboCache:
    return fiboCache[n]
  elif n == 1 or n == 0:
    return 1
  else:
    value = fib(n - 2) + fib(n - 1)

  fiboCache[n] = value  # daha buraya kadar return etmedik; ilk ekliyoruz

  # Burada o değeri depoladıktan sonra dönüyoruz
  return fib(n - 1) + fib(n - 2)
