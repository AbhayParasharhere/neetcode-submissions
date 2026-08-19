class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # have 2 pointes at teh start of both text
        # if tehy re equal we move both pointers
        # now we have 2 chocies we take both, and between our branches choose the one wher we find highest matches
        # if any go out of bound i or j we return 0 and stop
        m = len(text1)
        n = len(text2)
        cache = {}
        def solve(i,j):
            if (i,j) in cache: return cache[(i,j)]
            if i >= m or j >= n: return 0
            res = 0
            if text1[i] == text2[j]:
                res = 1 + solve(i+1,j+1)
            else:
                move_i = solve(i+1,j)
                move_j = solve(i,j+1)
                res = max(move_i,move_j)
            cache[(i,j)] = res
            return res
        # return solve(0,0)
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i][j] = 1+(dp[i-1][j-1] if i - 1 >= 0 and j -1 >= 0 else 0)
                else:
                    move_i = dp[i-1][j] if i - 1 >= 0 else 0
                    move_j = dp[i][j-1] if j - 1 >= 0 else 0
                    dp[i][j] = max(dp[i][j],move_i,move_j)
        return dp[m-1][n-1]


