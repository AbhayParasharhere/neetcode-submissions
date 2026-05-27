class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # asnwer space - max sum is a montonic split where we have a scheme where we had chosen the minium partiotn
        # all other schemes in here is that parttiotn scheme used resulted in a sum grater than teh minimum
        # all trues first position gives us the minium
        # all the false are such that the partition shceme used 
        # cannot be done in a sum that uses k or few partition splits
        n = len(nums)
        l = max(nums)
        r = sum(nums) + 1

        def sumPossibleinK(target):
            partitionSplits = k - 1 #-1 due to counting teh wedges logic
            sum_so_far = 0
            for num in nums:
                if num + sum_so_far > target:
                    partitionSplits -= 1
                    # used a partition split
                    sum_so_far = num 
                else:
                    sum_so_far += num
            return partitionSplits >= 0

        while l < r:
            m = (l+r) // 2
            if sumPossibleinK(m): r = m
            else: l = m + 1
        # no need to check l is last as answer is guaranteed
        return l