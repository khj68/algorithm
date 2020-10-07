def chae(n):
  check = [False,False] + [True]*(n-1)
  primes = []

  for i in range(2, n+1):
    if check[i]:
      primes.append(i)
      for j in range(2*i, n+1, i):
        check[j] = False

  # print(primes)
  return primes

n = int(input())

nums = chae(n)

l = 0
r = 0
ans = 0
cur = 0

while True:
  # print(l, r, cur, ans)
  if cur == n:
    ans += 1
    cur -= nums[l]
    l += 1
  elif cur > n:
    cur -= nums[l]
    l += 1
  elif cur < n:
    if r == len(nums): break
    cur += nums[r]
    r += 1

print(ans)