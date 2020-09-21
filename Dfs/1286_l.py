class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.li = []
        def dfs(k, path):
            if (len(path) == combinationLength):
                self.li.append(path)
                return
            for i in range(k+1, len(characters)):
                dfs(i, path+characters[i])
        dfs(-1, '')
        self.i = -1
        
    def next(self) -> str:
        self.i += 1
        return self.li[self.i]

    def hasNext(self) -> bool:
        return self.i < len(self.li)-1


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()