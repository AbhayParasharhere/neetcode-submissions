class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n

        while l < r:
            m = (l+r) // 2

            if nums[m] <= nums[n-1]: r = m
            else: l = m + 1
        return nums[l]