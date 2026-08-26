class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # insteaf of first baloon to burst which deosnt split right and left half into independent probkems
        # ask what is the alst baloon to ppop then the second last baloons isnt a dependent problm - it directly depnds on the alst baloon for one oits boundary so now the left and right half are independent

        # isnert 1 for off boudn indexing propely
        nums = [1] + nums + [1]
        n = len(nums)
        cache = {}
        def solve(i,j):
            if (i,j) in cache: return cache[(i,j)]
            # no subprob to solve
            if i > j: return 0

            res = float('-inf')
            # any one of the balloon can be the balon to burst at this step
            for p in range(i,j+1):
                coins_from_burst = nums[i-1] * nums[p] * nums[j+1]
                # now we move from this step to one step before 
                lt_partition = solve(i,p-1)
                rt_partition = solve(p+1,j)
                branch_coins = coins_from_burst + lt_partition + rt_partition
                res = max(branch_coins,res)
            cache[(i,j)] = res
            return res


        # return solve(1,n-2)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        # i goes from 1 to n-2 in rec so here in dp from n-2 to 1
        # j from n-2 to 1 in rec so ehre in dp from 1 to n -2
        for i in range(n-2,0,-1):
            for j in range(1,n-1):
                if i > j: dp[i][j] = 0
                else:
                    dp[i][j] = float('-inf')
                     # any one of the balloon can be the balon to burst at this step
                    for p in range(i,j+1):
                        coins_from_burst = nums[i-1] * nums[p] * nums[j+1]
                        # now we move from this step to one step before 
                        lt_partition = dp[i][p-1]
                        rt_partition = dp[p+1][j]
                        branch_coins = coins_from_burst + lt_partition + rt_partition
                        dp[i][j] = max(branch_coins,dp[i][j])
        return dp[1][n-2]
