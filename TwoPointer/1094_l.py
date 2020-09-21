class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        li = []
        
        for n, s, e in trips:
            li.append((s, n))
            li.append((e, -n))
        li.sort()
        
        cur = 0
        for _, cnt in li:
            cur += cnt
            if cur > capacity:
                return False
        
        return True