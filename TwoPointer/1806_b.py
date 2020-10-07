n, m = map(int, input().split())

nums = list(map(int, input().split()))

l = 0
r = 0
ans = 100000000000000
cur = 0

# nums.sort()

while True:
  if cur >= m:
    ans = min(ans, r-l)
    cur -= nums[l]
    l += 1
  elif cur < m:
    if r == n: break
    cur += nums[r]
    r += 1

if ans == 100000000000000:
  print(0)
else: print(ans)