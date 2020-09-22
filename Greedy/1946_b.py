T = int(input())

for _ in range(T):
    n = int(input())
    li = []
    for _ in range(n):
        li.append(tuple(map(int, input().split())))
    li.sort()
    m = li[0][1]
    cnt = 1

    for i in range(1, len(li)):
        if li[i][1] < m:
            cnt += 1
            m = li[i][1]
    print(cnt)

