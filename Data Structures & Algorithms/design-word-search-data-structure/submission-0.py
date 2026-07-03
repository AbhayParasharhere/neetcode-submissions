class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        # standard trie add
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = WordDictionary()
            node = node.children[c]
        node.is_end = True

    # we need a fx that takes in node as well as node is shrinking in each call as well
    def dfs(self,node,word):
        # print(word,t.children,"\n")
        if not node: return False
        for i, c in enumerate(word):
            if c not in node.children:
                if c == ".":
                    remainder = word[i+1:]
                    for child in node.children.values():
                        # visist every branch
                        if self.dfs(child,remainder):
                            return True
                return False
            node = node.children[c]
        return node.is_end

    def search(self, word: str) -> bool:
        # in here the only special case is that when we have a .
        # we want to search in all possible branches - so we can do a recursive call
        # to search with the remainedr of the word after the .
        root = self
        return self.dfs(root,word)
        
