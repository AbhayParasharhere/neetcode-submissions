class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # shrink condiion when sum of window is target or greater
        # calculate res tehn and there

        l = 0
        n = len(nums)
        r = n
        tot = 0
        res = float('inf')
        for r in range(n):
            tot += nums[r]
            while tot >= target:
                res = min(res,r-l+1)
                tot -= nums[l]
                l += 1
        if res == float('inf'): return 0
        return res