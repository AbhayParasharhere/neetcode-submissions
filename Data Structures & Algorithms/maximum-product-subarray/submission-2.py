class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # at tevery index i 
        # ask yourself if i include i whats the max subarray sum from the start
        # and also ask whats the minimum subarray sum till index i
        # both info necessary fro multiplication problems as -ve requries min to create anotehr positive

        maxm = nums[0]
        minm = nums[0]
        res = maxm

        for num in nums[1:]:
            # till index i
            # either from extending the maximum subarray total, or the minm subarray total to n
            # or just takings igular num by itself at i, choose whatver is teh maxm out of those 3
            # so asking extending teh maxm subarray from before to num, minm subarrya to num or just keeping num by itself at index i for the best and worst answer
            if num == 0:
                maxm, minm = 1, 1
            temp = num*maxm
            maxm = max(num*maxm,num*minm,num)
            minm = min(temp,num*minm,num)
            res = max(res,maxm)
        return res