class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[1]*n]
        for i in range(m-1):
            arr.append([1] + [0]*(n-1))
            
        for r in range(1, m):
            for c in range(1, n):
                arr[r][c] = arr[r-1][c] + arr[r][c-1]
                
        return arr[m-1][n-1]
                