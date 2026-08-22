class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        cache = {}
        def solve(i,j):
            if (i,j) in cache: return cache[(i,j)]
            # all stones picked
            if i > j: return 0

            # since paleyr based - works fine alice max is bob min 
            # we track al - bob score
            pick_i = piles[i] - solve(i+1,j)
            pick_j = piles[j] - solve(i,j-1)
            res = max(pick_i,pick_j)
            cache[(i,j)] = res
            return res
        return True if solve(0,n-1) > 0 else False
