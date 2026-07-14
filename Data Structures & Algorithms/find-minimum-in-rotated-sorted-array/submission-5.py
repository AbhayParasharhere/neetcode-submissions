class Solution:
    def findMin(self, nums: List[int]) -> int:
        # minimum monotonus such taht eveyrthing from minum is less than or euql to end

        l = 0
        n = len(nums)
        r = n

        while l < r:
            m = (l+r) // 2
            if nums[m] <= nums[n-1]: r = m
            else: l = m + 1
        return nums[l]