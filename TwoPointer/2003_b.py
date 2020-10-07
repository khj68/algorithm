n, m = map(int, input().split())

nums = list(map(int, input().split()))

l = 0
r = 0
ans = 0
cur = 0

# nums.sort()

while True:
  if cur == m:
    ans += 1
    cur -= nums[l]
    l += 1
  elif cur > m:
    cur -= nums[l]
    l += 1
  elif cur < m:
    if r == n: break
    cur += nums[r]
    r += 1

print(ans)