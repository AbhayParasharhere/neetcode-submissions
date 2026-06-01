class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # one streaight forward solition is when you are moving the k sized sldiing window
        # is to use a monotonic stack

        stack = deque()
        l= 0
        n = len(nums)
        res = []

        for r in range(n):
            # print(stack)
            to_put = nums[r]
            # to maintain stack montonocity
            # max index is at the top
            while stack and nums[stack[-1]] < to_put:
                stack.pop()
            stack.append(r)        
            
            if r - l + 1 > k:
                # This deque follwos a very nice structure
                # it keeps track of max win element on top
                # as we slide window we can pop the outdated index from the start
                l += 1
                if stack[0] < l: stack.popleft()
            if r - l + 1 == k:
                res.append(nums[stack[0]])
        return res
        

            
                
