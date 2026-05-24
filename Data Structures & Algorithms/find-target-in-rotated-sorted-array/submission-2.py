class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search to find the position of te minium element thats our partition pt
        # after that call bs with the target in teh appropirate partition
        #  min numebr in sorted array such that nums[m] <= nums[r]

        # Find teh min index for partition
        n = len(nums)
        l = 0
        r = n

        while l < r:
            m = (l+r) //2
            if nums[m] <= nums[n-1]: r = m
            else: l = m + 1

        partition = l
        l = 0
        r = n

        def bs(l,r):
            bound = r
            while l < r:
                m = (l+r) // 2
                if nums[m] >= target: r = m
                else: l = m + 1
            if l >= bound or nums[l] != target: return -1
            else:
                return l

        if target > nums[r-1]:
            # BS the lt half
            # print('lt',l,partition)
            return bs(l,partition)
        else:
            # BS the right half
            # print('rt',partition,r)
            return bs(partition,r)