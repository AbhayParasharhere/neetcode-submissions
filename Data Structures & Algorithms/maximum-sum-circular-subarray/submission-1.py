class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # taking the special case since array is wrppped is litrally teh minim subarray sum - total - we exclude teh center which contains minm part and take everything else
        tot = sum(nums)

        cur_max = cur_min = max_best = min_best = nums[0]
        # kadane for minm and maxium
        for num in nums[1:]:
            # start fresh at num or keep extedning cur
            cur_max = max(num,cur_max+num)
            max_best = max(max_best,cur_max)

            cur_min = min(num,cur_min+num)
            min_best = min(min_best,cur_min)
        
        wrap_best = tot - min_best
        if wrap_best == 0:
            return max_best
        # print(max_best,wrap_best,min_best)
        return max(wrap_best,max_best)