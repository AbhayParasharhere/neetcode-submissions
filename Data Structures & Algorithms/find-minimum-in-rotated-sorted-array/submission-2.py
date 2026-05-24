class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = len(nums) - 1
        # edge case no roation
        if nums[l] <= nums[r]: return nums[l] 

        while l < r:
            m = (l+r) // 2
            if nums[m] <= nums[r]: r = m
            else: l = m + 1

        return nums[l] 