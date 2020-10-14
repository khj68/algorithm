from bisect import bisect_left
import time

def segment(x, space):
    s = time.time()
    m = min(space[:x])
    m_idx = bisect_left(space[:x], m)
    ans = m

    for i in range(x, len(space)):
        if i-x >= m_idx:
            m = min(space[i-x+1:i+1])
            m_idx = bisect_left(space[i-x+1:i+1], m)
            ans = max(m, ans)
        elif space[i] < m:
            m_idx = i
            ans = max(m, ans)

    # if not ans:
        # return min(space)
    print('time : ', time.time() - s)
    return ans


print(segment(1, [1,2,3,1,2]))
print(segment(2, [1,1,1]))
print(segment(3, [2,5,4,6,8]))
print(segment(5, [2,5,4,6,8]))

import random
li = [random.randint(1, 100000000) for _ in range(1000000)]
print(segment(1000, li))