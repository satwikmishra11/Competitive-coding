class Solution:
  def kthFactor(self, n: int, k: int) -> int:
    factor = 1
    i = 0  

    while factor < math.isqrt(n):
      if n % factor == 0:
        i += 1
        if i == k:
          return factor
      factor += 1

    factor = n // factor
    while factor >= 1:
      if n % factor == 0:
        i += 1
        if i == k:
          return n // factor
      factor -= 1

    return -1
