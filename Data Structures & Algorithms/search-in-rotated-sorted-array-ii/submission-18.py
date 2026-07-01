class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # find the monotonicity such that elments before the pivot are greater than the last element
        # we find the first true element

        n = len(nums)
        l = 0
        r = n
        if n == 1: return nums[0] == target

        # in case of last element wrapping aroound the start cos of duplicates
        # we need to move l forward until it doesnt match the start
        while l < r and nums[l] == nums[r-1]:
            l += 1
        
        while l < r:
            m = (l+r) // 2
            if nums[m] <= nums[n-1]: r = m
            else: l = m + 1
        
        pivot = l
        def search(l,r):
            # print(l,r,nums[l])
            bound = r
            while l < r:
                m = (l+r) // 2
                if nums[m] >= target: r = m
                else: l = m + 1
            if l == bound or nums[l] != target:
                return False
            return True
        if target <= nums[n-1]: 
            # search after the pivot including pivot
            return search(pivot,n)
        else:
            # search before the pivot
            return search(0,pivot)
