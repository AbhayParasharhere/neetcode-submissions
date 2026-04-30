class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1 0 1 2 to [0 1 1 2]
        # note the 3 groups we only have 3 things - this must give some insight
        # we can use 3 pointers to keep track of each of these 3 groups of 0,1,2
        # 0p start at the start, 2p start at the end, remaining stuff is left in the middle is naturally 1
        # we use a loop pointer - this is from instinct from solving this question previosuly
        # the right 2p pointer naturally aligns itslef to the last 2 from the rt, the left 0p pointer aligns to the rightmost 0
        # the loop pointer then works magically if it sees a 0 it swaps with the 0p pointer and move it forward
        # 1 0 1  2 => 2 at j end which is correct so j moves on => 1 0 1 2
        # ip     j                                                 i p j 
        # p at 0 swap with i and move i forward, keep p there
        # 0 1  1 2
        #   ip j
        #  when p and j meet it means everythig is done

        i = 0 # for the 0 group
        j = len(nums) - 1 # for the 2 group
        p = 0 # loop pointer
        while p <= j:
            if nums[p] == 0:
                nums[i], nums[p] = nums[p], nums[i]
                i += 1
                p += 1
                # Only in swap with 2 case we dont advance as 
            elif nums[p] == 2:
                nums[j], nums[p] = nums[p], nums[j]
                j -= 1
            else: # 1 case
                p += 1
        


        
        