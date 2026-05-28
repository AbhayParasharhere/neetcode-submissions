class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Speiacial case whre we need to trim the starting element if same to teh last
        # why cos last is our method to check for partioin pot

        n = len(nums)
        r = n
        l = 0
        while l<r and n > 1 and nums[n-1] == nums[l]:
            l += 1
    
        while l < r:
            m = (l+r) // 2
            if nums[m] <= nums[n-1]: r = m
            else: l = m + 1
        
        if l == n: return False

        partition = l

        def bs(l,r):
            bound = r
            while l < r:
                m = (l+r) // 2
                if nums[m] >= target: r = m
                else: l = m + 1
            if l == bound: return False
            return nums[l] == target

        if target > nums[n-1]:
            return bs(0,partition)
        else:
            return bs(partition,n)
        

