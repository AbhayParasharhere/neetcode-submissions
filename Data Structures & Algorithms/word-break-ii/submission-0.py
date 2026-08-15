class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # first get wordidct into a dict for quick lookup
        hset = set()
        for w in wordDict:
            hset.add(w)

        res = []
        n = len(s)
        cache = {}

        def backtrack(at,path):
            if at >= n:
                res.append(" ".join(path))
                return

            # check every substring
            # form word
            w = ""
            for j in range(at,n):
                w += s[j]
                # print(w)
                if w not in hset: continue
                # add to path
                path.append(w)
                backtrack(j+1,path)
                path.pop()
        backtrack(0,[])
        return res



