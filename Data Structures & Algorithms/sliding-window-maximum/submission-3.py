class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # using teh deque apporach and a manotonic stack where the amx stays at the bottom
        # when we slide if l is greater than the index of this max
        # we pop it from the left now our deque points to next max which is 
        # correct fror the next window
        n = len(nums)
        res = []
        l = 0
        deq = deque()

        for r in range(n):
            # print(deq,'r',r)
            # put the element mainiating montonicity
            # anything less gets eliminated keeping greater there
            num = nums[r]
            while deq and nums[deq[-1]] < num:
                deq.pop()
            deq.append(r) # we store index for later easy comparision when popping
                
            # slide the window when it reaches k size
            if r - l + 1 >= k:
                # First put the max which is at the bottom of deque
                # print(deq,nums[deq[0]],deq[0],'put',l,r)
                res.append(nums[deq[0]])
                l += 1
                if deq[0] < l: deq.popleft()
        return res
