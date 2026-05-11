class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a + b + c = 0 so b + c = - a
        # so sort then use two ptr 2 sum approach to find -a fixed target 
        # this target moves eventually through the entrie array and we always look ahead for l and r 
        # the reason we look ahead is becuase elements to teh left have already been cehcked 
        # as they had been target before
        nums.sort()
        res = set()
        for i,num in enumerate(nums):
            target = -1 * num
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.add(tuple([num,nums[l],nums[r]]))
                    l += 1
                    r -= 1 
        return [list(triplet) for triplet in res]
            
