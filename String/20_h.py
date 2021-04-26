class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '{': '}', '[': ']', ')': '(', ']': '[', '}': '{'}
        openb = ('(', '{', '[')
        closeb = (')', '}', ']')
        stack = []
        for c in s:
            if c in openb:
                stack.append(c)
            else:
                if not stack or stack.pop() != d[c]:
                    return False
                
        return stack == []
    