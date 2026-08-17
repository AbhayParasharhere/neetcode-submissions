class Solution:
    def longestPalindrome(self, s: str) -> str:
        # use tempplate to find all i,j substrings that are olindrome, whatevr i j diff is largetst return that as res

        n = len(s)
        if n <= 1: return s
        dp = [[False for _ in range(n)] for _ in range(n)]
        resL = 0
        res = s[0]
        for L in range(1,n+1):
            i = 0
            while i + L - 1 < n:
                j = i + L - 1
                if i == j: dp[i][j] = True
                elif i + 1 == j: dp[i][j] = s[i] == s[j]
                else: dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                if abs(i-j) > resL and dp[i][j]:
                    resL = abs(i-j)
                    res = s[i:j+1]
                i += 1
        return res