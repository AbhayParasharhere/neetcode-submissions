class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Earlier version was solved using the voting algorithm
        # Now we can have multiple results - all who appear more than n /3
        # Question how many such elemnts who are more than n / 3 - as 3n/3 = n therefore atmost 2
        # 5 2 3     2 2 2 2 5   5 5
        # x y x-1=x y y y y x-1 x x
#Votes  # 1 1 1     2 3 4 5. 1. 2 3
        # return x and y 2,5   
        # we need to keep track of 2 majority element votes say - x and y
        # Critical question is when a vote comes which is not x nor y - do we subtract from both x and y or the lower between x and y
        # lets subtract from both x and y

        # Initially when you encounter first vote which is not for x - make it vote for y
        # If both xv and yv are 1 or less than 1 then return []
        x = nums[0]
        xv = 1
        y = None
        yv = 0

        for num in nums[1:]:
            if num == x:
                xv += 1
            elif y is not None and num == y:
                yv += 1
            elif num != x or num != y:
                if y is None:
                    y = num
                    yv = 1
                    continue
                if xv == 0:
                    x = num
                    xv = 1
                elif yv == 0:
                    y = num
                    yv = 1
                xv -= 1
                yv -=1
        res = []
        for candidate in [x, y]:
            if candidate is not None and nums.count(candidate) > len(nums) / 3:
                res.append(candidate)
        return res
