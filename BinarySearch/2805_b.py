from bisect import bisect
n, m = map(int, input().split())

trees = list(map(int, input().split()))

trees.sort()
l = 0
r = trees[-1]
ans = 0

while l<=r:
  mid = (l+r) // 2
  idx = bisect(trees, mid)
  cur = sum(tree-mid for tree in trees[idx:])

  if m > cur:
    r = mid-1
  elif m < cur:
    ans = mid
    l = mid+1
  else:
    ans = mid
    break


print(ans)