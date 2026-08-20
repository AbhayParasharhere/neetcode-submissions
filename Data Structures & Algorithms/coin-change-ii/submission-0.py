class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # combination question with repeat allowed - perm will giev us duplicate leaves
        # for i,j and j,i both hence we will overcount
        # we need to count branches where we have 1

        cache = {}
        n = len(coins)
        def solve(i,left):
            if (i,left) in cache: return cache[(i,left)]
            if left == 0:
                return 1
            elif left < 0:
                return 0
            res = 0
            for j in range(i,n):
                res += solve(j,left-coins[j])
            cache[(i,left)] = res
            return res
        return solve(0,amount)