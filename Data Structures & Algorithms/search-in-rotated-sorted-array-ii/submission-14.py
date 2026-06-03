class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # need to strip anything equal to end from the start
        n = len(nums)
        l = 0
        r = n

        while n > 1 and l < n and nums[l] == nums[r-1]:
            l += 1
        
        # find partition
        while l < r:
            m = (l+r) // 2
            if nums[m] <= nums[n-1]: r = m
            else: l = m + 1
        partition = l
        
        def bs(l,r):
            bound = r
            while l < r:
                m = (l+r) // 2
                if nums[m] >= target: r =m
                else: l = m + 1
            if l == bound: return False
            return nums[l] == target

        
        if target > nums[n-1]: return bs(0,partition)
        else: return bs(partition,n)
