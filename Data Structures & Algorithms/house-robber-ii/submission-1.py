class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}
        def solve(i,nums):
            if i in cache: return cache[i]
            if i <= 0: return 0
            # we can either rob this house or skip it
            # if rob we cannot rob the next house but house i -2
            rob = nums[i-1] + solve(i-2,nums)
            skip = solve(i-1,nums)
            cache[i] = max(rob,skip)
            return cache[i]
        # now you cannot rob 1st and last house as they are connected
        # if u rob h1 then range is for 0 to n-1
        # if u rob h2 then from 1 to n

        h1_rob = solve(n-1,nums[0:n])
        cache = {}
        h1_skip = solve(n-1,nums[1:])
        if n == 1: return nums[0]
        return max(h1_rob,h1_skip)