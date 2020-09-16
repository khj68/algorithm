class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        rightmost = {c:i for i, c in enumerate(S)}
        left, right = 0, 0
        
        res = []
        for i, letter in enumerate(S):
            right = max(right, rightmost[letter])
            
            if i == right:
                res += [right-left + 1]
                left = i+1
        
        return res