from collections import Counter
from collections import deque
from functools import reduce
import bisect
import heapq
import math

def solution(U, L, C):
    length = len(C)
    upper_arr = [0] * length
    lower_arr = [0] * length
    upper_cnt = 0
    lower_cnt = 0

    for i, num in enumerate(C):
        if num == 2:
            upper_arr[i] = 1
            lower_arr[i] = 1
            upper_cnt += 1
            lower_cnt += 1
    
    for i, num in enumerate(C):
        if num == 1:
            if upper_cnt < U:
                upper_arr[i] = 1
                upper_cnt += 1
            elif lower_cnt < L:
                lower_arr[i] = 1
                lower_cnt += 1
                
    if U != upper_cnt or L != lower_cnt:
        return 'IMPOSSIBLE'

    return ''.join(map(str, upper_arr)) + ',' + ''.join(map(str, lower_arr))

print(solution(2, 3, [0, 0, 1, 1, 2]))