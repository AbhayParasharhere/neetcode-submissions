class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minS = float('inf')
        l = 0
        tot = 0

        for r in range(len(nums)):
            # here total is our window
            tot += nums[r]

            while tot >= target:
                minS = min(minS,r-l+1)
                tot -= nums[l]
                l += 1
        if minS == float('inf'): return 0
        return minS
