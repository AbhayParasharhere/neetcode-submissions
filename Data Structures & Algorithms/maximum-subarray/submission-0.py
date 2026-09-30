class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        max_best = nums[0]

        for num in nums[1:]:
            # start at num new array or keep extending from cur
            cur = max(num,num+cur)
            max_best = max(max_best,cur)
        return max_best