n = int(input())
leftList = list(map(int, input().split()))
ans = [0] * n

for k, left in enumerate(leftList):
    left += 1
    for i in range(n):
        if ans[i]: continue
        left -= 1
        if left < 1:
            ans[i] = k+1
            break
    # print(k, left, ans)

print(*ans)