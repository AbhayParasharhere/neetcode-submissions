class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        dp = [[False for _ in range(n)] for _ in range(n)]
        # we use a dp table that says i,j is a palin or not for a quick lookup in our backtracking fx

        for L in range(1,n+1):
            i = 0
            while i + L - 1 < n:
                j = i + L - 1
                if i == j: dp[i][j] = True
                elif i + 1 == j: dp[i][j] = s[i] == s[j]
                else: dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                i += 1


        # i starts at 1
        def backtrack(i,path):
            print(i,path)
            if i == n:
                # in path append wahtever else ise left after i
                res.append(path[:])
                return


            for p in range(i,n):
                if not dp[i][p]: continue
                #  we know this part is palin so push to path
                path.append(s[i:p+1])
                backtrack(p+1,path)
                path.pop()
        backtrack(0,[])

        return res
            

