class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Need to split teh duplicates to the start that match with the end
        # the end is used to find the minimum point or the partition point of the
        # rotated array
        # After we have the min point we can find teh right half to search the target

        # Strip the duplicates at the start if match the end
        n = len(nums)
        l = 0
        r = n

        if n == 1: return nums[0] == target
        while l < n and r > 0 and nums[l] == nums[r-1]:
            l += 1
        # Now we have correct l, find the min point or partition now
        while l < r:
            m = (l + r) // 2
            if nums[m] <= nums[n-1]: r = m
            else: l = m + 1
        partition = l
        # print(l,r,partition)
        l = 0
        r = n
        def bs(l,r):
            bound = r
            while l < r:
                m = (l + r) //2
                if nums[m] >= target: r = m
                else: l = m + 1 
            # print(nums[l],target,bound,l == bound,l)
            if l == bound: return False
            return nums[l] == target

        if target > nums[r-1]:
            # in the left half
            return bs(l,partition)
        else:
            # in the right half
            # print('rt')
            return bs(partition,n)

