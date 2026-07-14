class PrefixTree:

    def __init__(self):
        self.is_end = False
        self.children = {}

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                # create new node
                node.children[c] = PrefixTree()
            node = node.children[c]
        # last is the end mark it
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        # no need to worry about the end marker, just the fact we matched 
        # with the whole word prefix is fine
        return True
        
        