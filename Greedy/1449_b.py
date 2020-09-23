n, l = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()
cur = 0
cnt = 0
for num in nums:
    if num > cur:
        cnt += 1
        cur = num + l - 1

print(cnt)