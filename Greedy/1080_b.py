n, m = map(int, input().split())
a, b = [], []
s = [[0]*m for i in range(n)]

def solve():
    cnt = 0
    for i in range(n-2):
        for j in range(m-2):
            if s[i][j] == False:
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        s[k][l] = not s[k][l]
                cnt += 1
    for i in range(n):
        for j in range(m):
            if s[i][j] == False:
                return -1
    return cnt

for i in range(n):
    a.append(list(input()))
for i in range(n):
    b.append(list(input()))
for i in range(n):
    for j in range(m):
        s[i][j] = a[i][j] == b[i][j]
if n >= 3 and m >= 3:
    print(solve())
else:
    for i in range(n):
        for j in range(m):
            if s[i][j] == False:
                print(-1)
                exit()
    print(0)
