class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        d = self.d
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['.'] = True
                

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        d = self.d
        for c in word:
            if c not in d:
                return False
            d = d[c]
        if '.' in d:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        d = self.d
        for c in prefix:
            if c not in d:
                return False
            d = d[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)