class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = 0
        for L in range(1,n+1):
            i = 0
            while i + L - 1 < n:
                j = i + L - 1
                if i == j: dp[i][j] = True
                elif i + 1 == j: dp[i][j] = s[i] == s[j]
                else: dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                if dp[i][j]: res += 1
                i += 1
        return res

