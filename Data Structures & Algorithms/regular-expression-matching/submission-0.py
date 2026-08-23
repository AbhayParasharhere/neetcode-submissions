class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        cache = {}
        def solve(i,j):
            if (i,j) in cache: return cache[(i,j)]

            # run out of pattern then the string - we return True
            if j >= m:
                if i >= n: return True
                return False
            res = False
            # check if the next element is a *
            if j+1 < m and p[j+1] == "*":
                # now we can take 0 or more elements depedns on how many matching char we can find
                ch2match = p[j]
                k = 0
                while True:
                    # move past the star to the next char to match 
                    # after we do all the branches
                    if solve(i+k,j+2):
                        res = True
                        cache[(i,j)] = res 
                        return True
                    if i + k >= n or not (s[i+k] == ch2match or ch2match == "."): break                    
                    k += 1
            else:
                # next elem is not a * simple matching case
                if i < n and ((s[i] == p[j]) or p[j] == "."):
                    if solve(i+1,j+1):
                        res = True
                        cache[(i,j)] = res 
                        return True
            cache[(i,j)] = res
            return res


        return solve(0,0)