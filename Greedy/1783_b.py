r, c = map(int, input().split())
if r == 1 :
    print(1)
elif r == 2:
    print(min(4, (c+1)//2))
elif c < 7:
    print(min(4, c))
else:
    print(c-2)
