class PrefixTree:

    def __init__(self):
        self.is_end = False
        self.children = {}

    def insert(self, word: str) -> None:
        # root is a dummy
        node = self
        for c in word:
            if c not in node.children:
                # create a children than with that key and with empty trie
                node.children[c] = PrefixTree()
            # advance to next relevant node child matching the character
            node = node.children[c]
        # in the end mark it as the end
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
        # instead of checking end with as with normal search just checking that we have 
        # the word so far is enough as it satisfies the prefx conditon
        return True
        
        