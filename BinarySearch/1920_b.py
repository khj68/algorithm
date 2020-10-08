from bisect import bisect_left


n = int(input())
nums = list(map(int, input().split()))

m = int(input())
finds = list(map(int, input().split()))

nums.sort()

for find in finds :
  idx = bisect_left(nums, find)
  # print(idx)
  if idx < n and nums[idx] == find:
    print(1)
  else:
    print(0)

