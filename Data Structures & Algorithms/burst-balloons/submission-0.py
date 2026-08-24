class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # we append 1 to make indexing easier as out of bounds ballon gets 1 multiplied

        # a bottom up dp apporach we we ask who is the last baloon to be busrt
        # could be anyone
        # one step above that that ballon is definelty tehre which was last burst and now it could be combined with anonye else who survived the 2nd last step
        # so now we hav a subporblem that only depends on the prev problem solved and not anything else
        nums = [1] + nums + [1]
        n = len(nums)
        memo = {}
        def solve(i,j):
            # no subporb to solve no coins
            if (i, j) in memo:
                return memo[(i, j)]
            if i > j: return 0
            maxi = float('-inf')
            for p in range(i,j+1):
                coins =  nums[i-1] * nums[p]  * nums[j+1]
                left_part = solve(i,p-1)
                right_part = solve(p+1,j)
                branch_cost = coins+ left_part+right_part

                if(branch_cost > maxi): maxi = branch_cost
            memo[(i, j)] = maxi
            return maxi
    
        return solve(1,n-2)