class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a deq which is a montonic decreasing stack, the deq 0 store sthe index of the max element
        # the deq size can atmost reach k
        # once the window slides if deq 0 index is less than l we pop the deq0 and put the new slided element onto the window deq

        d = deque()
        res = []
        n = len(nums)
        l = 0

        for r in range(n):
            # push the index in stack to maniantin montonic decreasing stack
            # if elem to put is 
            put = nums[r]
            while d and nums[d[-1]] < put:
                d.pop()
            d.append(r)

            if r - l + 1 > k:
                # we slide now that window size is greater than k
                # rigth now win size is k + 1
                l += 1
                # now its k but d could have outdated max the k+ 1th element
                if d[0] < l:
                    # we pop as its out of the window now
                    d.popleft()
            if r - l + 1 == k:
                res.append(nums[d[0]])
        return res


