n = int(input())
li = []
cnt = 0
cur = 0
for i in range(n):
    li.append(tuple(map(int, input().split())))

# print(li)
li.sort(key = lambda x: x[0])
li.sort(key = lambda x: x[1])
# print(li)

for s, e in li:
    if s >= cur:
        cur = e
        cnt += 1

print(cnt)