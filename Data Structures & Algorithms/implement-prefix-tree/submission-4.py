class TrieNode:
    def __init__(self,isEnd = False):
        self.isEnd = isEnd
        self.children = {}
        
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.children:
                return False
            # continue traversing
            cur = cur.children[w]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return True