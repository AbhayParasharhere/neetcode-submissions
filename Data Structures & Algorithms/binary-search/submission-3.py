class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0 , len(nums)

        while l < r:
            m = (l+r) // 2
            if nums[m] >= target: r = m
            else: l = m + 1
        
        if l==len(nums) or nums[l] != target: return -1
        
        return l