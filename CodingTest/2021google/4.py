from collections import Counter
from collections import deque
from functools import reduce
import bisect
import heapq
import math

def solution(A, B):
    A.sort()
    B.sort()
    i = 0
    for a in A:
        while i < len(B) - 1 and B[i] < a:
            i += 1
        if a == B[i]:
            return a
    return -1
