n, k = map(int, input().split())
cnt = 0
nums = []
for i in range(n):
    nums += [int(input())]

for num in nums[::-1]:
    cnt += k//num
    k %= num

    if not k: break

print(cnt)