class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        p = len(s3)
        if n+m != p: return False
        cache = {}

        def solve(i,j):
            if (i,j) in cache: return cache[(i,j)]
            if i == n and j == m and i+j == p: return True
            # case where one string is empty but still res produced entirely from 1 string
            if i+j == p: return False

            # take from s1 or s2 only from each if the char at i+j matches
            res = False
            if i < n and s3[i+j] == s1[i]:
                # now we can take thsi from s1
                res = solve(i+1,j)
            if res: 
                cache[(i,j)] = True
                return True

            if j < m and s3[i+j] == s2[j]:
                # can now take from s2
                res = solve(i,j+1)

            cache[(i,j)] = res
            return res
        return solve(0,0)

