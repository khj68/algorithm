class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.visit = [False] * len(tiles)
        self.res = set()
        
        def dfs(s):
            if s in self.res:
                return
            else: self.res.add(s)
            # print(self.res)
            for i in range(len(tiles)):
                if self.visit[i] : continue
                self.visit[i] = True
                dfs(s+tiles[i])
                self.visit[i] = False
        
        dfs('')
        return len(self.res) - 1
        
        
                