class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(i,comb,sum_left):
            if sum_left == 0: 
                res.append(comb[:])
                return
            elif sum_left < 0:
                # invalid cases
                return
            if i >= n:
                return
            
            for j in range(i,n):
                # dups allwoed so j instead of j + 1
                comb.append(nums[j])
                backtrack(j,comb,sum_left - nums[j])
                # retract choice - skip case called implicitly as loop advances in this
                # recursion frame after coming form recursion
                comb.pop()
        backtrack(0,[],target)
        return res
            