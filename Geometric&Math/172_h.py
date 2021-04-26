import math
def trailingZeroes(self, n: int) -> int:
  for i in range(1, 100):
    count = 0
    tmp = math.factorial(i)
    while tmp%5 == 0:
      tmp //= 5
      count += 1
    print(i, count)

    print(i, math.factorial(i))

trailingZeroes(0, 5)
