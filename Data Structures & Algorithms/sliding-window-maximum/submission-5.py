class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a deque - max stack pricniple to keep the max at the bototm of deque
        # when window slides pop it off if its index less than l, next stack[0] is the correct max then
        n = len(nums)
        l = 0
        dq = deque()
        res = []


        for r in range(n):
            # push index usch that maninating the order in the deque
            # where max is at the bottom
            num2check = nums[r]
            while dq and nums[dq[-1]] < num2check:
                dq.pop()
            dq.append(r)

            # shrink when we reach k length
            if r - l + 1 > k:
                # we need to slide
                l += 1
                if dq[0] < l: dq.popleft()
            if r - l + 1 == k:
                mx = nums[dq[0]]
                res.append(mx)
        return res

