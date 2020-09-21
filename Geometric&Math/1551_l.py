class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        if n % 2 == 0: # even
            tmp = 1
            for i in range(n//2):
                ans += tmp
                tmp += 2
        else: # odd
            tmp = 2
            for i in range(n//2):
                ans += tmp
                tmp += 2
        return ans