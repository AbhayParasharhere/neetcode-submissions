class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hmap = set()
        for w in wordDict: hmap.add(w)
        n = len(s)
        cache = {}
        # print(hmap)
        def solve(i):
            if i in cache: return cache[i]
            if i >= n: return True

            w = ""
            res = False
            for j in range(i,n):
                # w coantins fixed bound always from i to j so substring not subseq
                w += s[j]
                # check if w is present
                if w in hmap:
                    # now only we can recurse furtehr
                    # any branch that returns true we return true oeverall
                    if solve(j+1):
                        res = True
                else: continue
            cache[i] = res
            return res
        return solve(0)
