i = 1
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0: break

    ans = 0
    div, mod = divmod(v, p)
    ans += div * l
    ans += min(mod, l)

    print('Case %d: %d'%(i, ans))
    i += 1