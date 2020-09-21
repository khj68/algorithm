class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # c = Counter(s) - Counter(t)
        # print(c.values())
        return sum((Counter(s)-Counter(t)).values())