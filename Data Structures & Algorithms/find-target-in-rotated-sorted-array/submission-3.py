class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # fidn teh partition ppoint then based on it do teh bs on teh right part
        # partion point is the minium point where first true m < last element
        n = len(nums)
        l,r = 0, n

        while l < r:
            m = (l + r) // 2
            if nums[m] <= nums[n-1]: r = m
            else: l = m + 1
        partition = l

        def bs(l,r):
            bound = r
            while l < r:
                m = (l+r) //2
                if nums[m] >= target: r = m
                else: l = m + 1
            if l == bound: return -1
            return l if nums[l] == target else -1
        if target > nums[n-1]:
            return bs(0,partition)
        else:
            return bs(partition,n)