class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}
        def solve(i,last_num):
            if (i,last_num) in cache: return cache[(i,last_num)]
            if i >= n: return 0

            # take case only if this num is less tahn last num
            skip = solve(i+1,last_num)
            take = 0
            if last_num is None or nums[i] > last_num:
                take = 1 + solve(i+1,nums[i])
            cache[(i,last_num)] = max(take,skip)
            return cache[(i,last_num)]
        return solve(0,None)
