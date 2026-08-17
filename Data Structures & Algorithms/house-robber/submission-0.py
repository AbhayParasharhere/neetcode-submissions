class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}
        def solve(i):
            if i in cache: return cache[i]
            if i <= 0: return 0
            # we can either rob this house or skip it
            # if rob we cannot rob the next house but house i -2
            rob = nums[i-1] + solve(i-2)
            skip = solve(i-1)
            cache[i] = max(rob,skip)
            return cache[i]
        return solve(n)