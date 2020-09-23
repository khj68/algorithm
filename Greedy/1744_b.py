 
n = int(input())
negative, positive = [], []
zero = 0
 
for i in range(n):
    m = int(input())
    if m < 0:
        negative.append(m)
    elif m == 0:
        zero += 1
    else: # m > 0
        positive.append(m)
 
nl, pl = len(negative), len(positive)
negative.sort()
positive.sort(reverse=True)
res = []
# negative
for i in range(0, nl-1, 2):
    res.append(negative[i]*negative[i+1])
if nl % 2 == 1 and zero == 0:
    res.append(negative[nl-1])
# positive
for i in range(0, pl-1, 2):
    if positive[i] > 1 and positive[i+1] > 1:
        res.append(positive[i]*positive[i+1])
    else:
        res.extend([positive[i], positive[i+1]])
if pl % 2 == 1:
    res.append(positive[pl-1])
 
print(sum(res))
