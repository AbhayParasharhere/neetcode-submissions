class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Can think of partitioning as driving wedgres into the array
        # so k = 2 we drive one wedge we decide where thsi wedge would go 
        # each wedge could be between (0,n-1) exclusive and n - 1 must be the end
        # so k = 4 we have k -1 or 3 wedges
        # space between the wedges form subarray
        # the toatl sum of any subarray or answer space we have to minimize
        # falls between max(arr) --- sum(arr) thi sis monotonic
        # depends on our wedge placement to minimize this
        # condition for wedge placement or min sum is pattern 1 or first true
        # where the sum of subarray after all wedge placement is ??

        wedges = k - 1
        n = len(nums)
        l = max(nums)
        r = sum(nums) + 1

        def possibleInWedges(target):
            available = wedges
            till = 0
            total = 0
            for num in nums:
                # greedily put wedges
                if total + num > target:
                    total = num
                    available -= 1
                else:
                    total += num
            return available >= 0


        while l < r:
            m = (l + r) //2
            # condition such that after palcing wedge 
            # everything to the left of m is not feasible or sum of subarray
            # is that anything to teh left we run out of wedge
            # anyting to its right its possible to do with wedges or fewer
            if possibleInWedges(m): r = m
            else: l = m + 1
        
        return l
