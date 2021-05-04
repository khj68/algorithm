from collections import Counter
from collections import deque
from functools import reduce
import bisect
import heapq
import math

def solution(A):
    ans = 0
    num_flags = {}

    for num in A:
        flag = 1 if num > 0 else -1
        abs_num = abs(num)

        if abs_num in num_flags and flag != num_flags[abs_num]:
            ans = max(ans, abs_num)
        else:
            num_flags[abs_num] = flag
        
    return ans

print(solution([3, 2, -2, 5, -3]))
print(solution([1, 1, 2, -1, 2, -1]))
print(solution([1, 2, 3, -4]))
