class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # search the partition point with the first true apporach bs
        # then using that partition search the left and right partition
        n = len(nums)
        l = 0
        r = n

        # 2 pointer apporach to strip the dupliacet on the either ends
        # otherwise the partiotion find lgic deosnt work
        while l<n and r> 0 and n > 1 and nums[l] == nums[r-1]:
            l += 1

        while l < r:
            m = (l+r) //2
            if nums[m] <= nums[n-1]: r = m
            else: l = m + 1
    
        p_st = l

        def bs(l,r):
            bound = r
            while l < r:
                m = (l+r) // 2
                if nums[m] >= target: r = m
                else: l = m + 1
            if l == bound or nums[l] != target:
                return False
            return True

        if target > nums[n-1]:
            # search the left half
            return bs(0,p_st)
        else:
            return bs(p_st,n)

        # Now bs to the apporioate part
        # Print the partition
        print(p_st,p_end)