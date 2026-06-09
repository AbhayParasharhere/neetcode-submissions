class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # gwo the window until u get the sum
        # then keep shrinking from left until sum is stil greater or equal
        # ecalculate the res then and tehre
        n = len(nums)
        l = 0
        r = n
        tot = 0
        minR = float('infinity')

        for r in range(n):
            tot += nums[r]

            while tot >= target:
                # shrink
                minR = min(minR, r - l + 1)
                tot -= nums[l]
                l += 1
        return minR if minR != float('infinity') else 0