class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        cache = {}
        def solve(i,j):
            if (i,j) in cache: return cache[(i,j)]
            # means we have fully matched the word 2 - its contained within word1
            if j >= m:
                # exact match
                if i >= n: return 0
                # word1 might have extar character can be removed throght del
                else:
                    # tehse are the remove operations needed for n -i char left
                    return n - i
            # but we coulnt match word 2 - very unlikely but
            if i >= n: return m - j

            res = float('inf')
            # match case
            match = float('inf')
            if word1[i] == word2[j]: 
                res = solve(i+1,j+1)
            insert = 1 + solve(i,j+1)
            delete = 1 + solve(i+1,j)
            replace = 1 + solve(i+1,j+1)
            res = min(res,insert,delete,replace)
            cache[(i,j)] = res
            return res
        res = solve(0,0)
        return res 