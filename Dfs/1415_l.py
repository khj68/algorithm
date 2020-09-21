class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.domain = ['a','b','c']
        self.res = []
        def dfs(k, path):
            if len(path) == n:
                self.res.append(path)
                return
            
            for i in range(3):
                if i== k : continue
                dfs(i, path+self.domain[i])
        dfs(-1, '')
        
        
        if k > len(self.res): return ''
        
        return self.res[k-1]