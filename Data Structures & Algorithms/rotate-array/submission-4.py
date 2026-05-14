class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using the cyclic apporach where we keep chasing the elemnt we have moved 
        # from the correct poistion until we complete exactly n swaps for each element
        n = len(nums)
        k = k % n
        swaps = 0
        cycleStartAt = 0
        while swaps < n:
            curIdx = cycleStartAt
            curElm = nums[curIdx]
            while True:
                nextIdx = (curIdx + k) % n
                nextElm = nums[nextIdx]
                # move the cur element to its correct place
                nums[nextIdx] = curElm
                swaps += 1
                # now we have a ref to the swapped element we want to start from there
                curElm = nextElm
                curIdx = nextIdx
                if curIdx == cycleStartAt:
                    break
            cycleStartAt += 1
            if swaps == n:
                break

