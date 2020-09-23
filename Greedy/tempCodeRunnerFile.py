r, c = map(int, input().split())

if r < 3:
    print(c//2)
elif c < 7:
    print(4)
else:
    print(c-2)
