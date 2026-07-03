class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        root = self
        for c in word:
            if c not in root.children:
                root.children[c] = WordDictionary()
            root = root.children[c]
        root.is_end = True

    def _dfs(self,node,word):
        for i,c in enumerate(word):
            if c == ".":
                remainder = word[i+1:]
                return any(self._dfs(child,remainder) for child in node.children.values())
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end

    def search(self, word: str) -> bool:
        root = self
        return self._dfs(root,word)

        
