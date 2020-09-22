n = int(input())
ropes = []

for i in range(n):
    ropes += [int(input())]

ropes.sort()
m = 0

for i in range(n):
    m = max(m, n*ropes[i])
    n-=1

print(m)