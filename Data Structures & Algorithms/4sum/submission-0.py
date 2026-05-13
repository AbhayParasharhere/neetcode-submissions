class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        while i < len(nums):
            # we want to avoid duplicate fix 
            while i > 0 and i < len(nums) and nums[i -1] == nums[i]:
                i += 1
            if i >= len(nums):
                break
            fix = nums[i]
            find = target - fix
            
            # now we are looking for find
            # such that b + c + d = find
            if i + 1 < len(nums):
                j = i + 1
            while j < len(nums):
                # j + 1 means that first value of j regardless if its same as i is allowed
                while j > i + 1 and j < len(nums) and nums[j-1] == nums[j]:
                    j += 1
                if j >= len(nums):
                    break
                innerFix = nums[j]
                innerFind = find - innerFix

                # Now the l and r two pointer logic
                if j < len(nums):
                    l = j + 1
                    r = len(nums) - 1
                    while l < r:
                        if nums[l] + nums[r] < innerFind:
                            # Sum less move the left pointer
                            l += 1
                        elif nums[l] + nums[r] > innerFind:
                            r -= 1
                        else:
                            #  we found the 2 pairs, and since we have innerfix, and fix we have all 4
                            # Since tehre can be more pairs within these bounds move teh l and r
                            #  in order to continue to find more pairs
                            res.append([nums[l],nums[r],innerFix,fix])
                            l += 1
                            r -= 1
                            #  now skipping the duplciaet part for l and r
                            while l < r and nums[l] == nums[l-1]:
                                l += 1
                            while l < r and nums[r] == nums[r+1]:
                                r -= 1
                j += 1
            i += 1
        return res
                