class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # a 2 pointer matching apporach with take and skip for subsequences
        # return 1 when j is done and count all these leaves

        n = len(s)
        m = len(t)
        cache = {}
        def solve(i,j):
            if (i,j) in cache: return cache[(i,j)]
            if j >= m: return 1
            # at this point we tried all subseq but didnt work out
            if i >= n: return 0
            res = 0
            # now only we can take - this is take branch
            if(s[i] == t[j]):
                res += solve(i+1,j+1)
            # skip branch
            res += solve(i+1,j)
            cache[(i,j)] = res
            return res
        return solve(0,0)
