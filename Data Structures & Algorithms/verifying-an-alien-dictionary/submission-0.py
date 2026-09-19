class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hmap = {w:i for i,w in enumerate(order)}
        
        # we just need ocnsec pair check no need for pair 1 check with pair 3 as its transitive
        for i in range(len(words) - 1):
            j = i + 1
            w1 = words[i]
            w2 = words[j]

            for p in range(len(w1)):
                if p == len(w2):
                    # means w2 is a prefix of 21 but is afterwards
                    return False
                if w1[p] != w2[p]:
                    if hmap[w1[p]] > hmap[w2[p]]:
                        return False
                    break
        return True