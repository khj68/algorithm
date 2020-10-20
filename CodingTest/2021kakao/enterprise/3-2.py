import time

def segment(x, space):

    s = []
    n = len(space)
    left = [-1] * (n+1)
    right = [n] * (n+1)

    for i in range(n):
        while (len(s) != 0 and space[s[-1]] >= space[i]):
            s.pop()
        
        if (len(s) != 0):
            left[i] = s[-1]
        
        s.append(i)
    # print(left, right)
    while (len(s) != 0):
        s.pop()

    for i in range(n-1, -1, -1):
        while (len(s) != 0 and space[s[-1]] >= space[i]):
            s.pop()
        
        if (len(s) != 0):
            right[i] = s[-1]
        
        s.append(i)
    
    ans = [0] * (n+1)

    for i in range(n):
        l = right[i] - left[i] - 1
        ans[l] = max(ans[l], space[i])
    
    for i in range(n-1, 0, -1):
        ans[i] = max(ans[i], ans[i+1])
    
    # for i in range(1, n+1):
        # print(ans[i], end = " ")
    

    return ans[x]


print(segment(1, [1,2,3,1,2]))
print(segment(2, [1,1,1]))
print(segment(3, [2,5,4,6,8]))
print(segment(5, [2,5,4,6,8]))

import random
li = [random.randint(1, 100000000) for _ in range(1000000)]
print(segment(1000, li))