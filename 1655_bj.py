from bisect import bisect_left
n = int(input())
nums = []
# ans = []
for i in range(n):
    n = int(input())
    nums.insert(bisect_left(nums, n), n)
    # ans.append(nums[len(nums)//2 if len(nums)%2 == 1 else len(nums)//2 -1])
    print(nums[len(nums)//2 if len(nums)%2 == 1 else len(nums)//2 -1])
# print(ans)






################

import sys
import heapq#heapq는 최소힙만 지원한다 최대힙을 구현하기위해선 -를 곱해서 넣어 주고 꺼낼때 다시 -를 곱해준다
 
 
def middleheap(minheap,maxheap,x):#넣기만함
    if len(maxheap)==len(minheap):#같다면 max힙에 넣어준다
        heapq.heappush(maxheap,-x)
    else:#max힙이 크다면 minheap넣어 균형을 맞춰준다.
        heapq.heappush(minheap,x)
    if minheap and -maxheap[0]>minheap[0]:#minheap이 비어잇지않고 최대 힙의 루트는 항상 최소 힙의 루트보다 작게 유지해준다.
        #최대힙의 루트노드가 더크다면 스왑해주고 다시 힙구조로 만들어주어야한다.
        a=heapq.heappop(minheap)
        b=-heapq.heappop(maxheap)
        heapq.heappush(maxheap,-a)
        heapq.heappush(minheap,b)
 
 
n=int(sys.stdin.readline())
minheap,maxheap=[],[]
while n>0:
    n-=1
    middleheap(minheap,maxheap,int(sys.stdin.readline()))
    print(-maxheap[0])
