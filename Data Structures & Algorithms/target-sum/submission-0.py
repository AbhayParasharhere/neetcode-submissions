class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        n = len(nums)

        def solve(i,so_far):
            if (i,so_far) in cache: return cache[(i,so_far)]
            if i == n:
                if so_far == target:
                    return 1
                else:
                    return 0
            res = 0
            plus = solve(i+1,nums[i]+so_far)
            minus = solve(i+1,-nums[i]+so_far)
            res += plus + minus
            cache[(i,so_far)] = res
            return res
        return solve(0,0)
