class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        def isValid(i,j):
            chunk = s[i:j+1]
            if chunk[0] == '0': return False
            return 0 < int(chunk) <= 26 if chunk else False
        
        cache = {}
        def solve(i):
            if i in cache: return cache[i]
            if i == n:
                return 1
            res = 0
            for j in range(i,min(i+2,n)):
                if isValid(i,j):
                    res += solve(j+1)
            cache[i] = res
            return res
        return solve(0)