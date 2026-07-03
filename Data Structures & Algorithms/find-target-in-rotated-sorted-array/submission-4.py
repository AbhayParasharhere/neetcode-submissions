class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # we comapre to the last element elemnts beofre the min all if roatted are greater than it

        # we use first true thats our min

        l = 0
        r = n
        while l < r:
            m = (l+r) // 2
            if nums[m] <= nums[n-1]: r = m
            else: l = m + 1
        
        pivot = l

        def bs(l,r):
            bound = r
            while l < r:
                m = (l+r) // 2
                if nums[m] >= target: r = m
                else: l = m + 1
            if l == bound or nums[l] != target: return -1
            return l

        if target <= nums[n-1]:
            # search in the second half including pivot
            return bs(pivot,n)
        else:
            # search in first half not including pivot
            return bs(0,pivot)