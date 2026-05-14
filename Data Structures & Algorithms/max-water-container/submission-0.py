class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_till = 0
        while l < r:
            max_till = max(max_till,(r - l) * min(heights[l],heights[r]))
            # trying to move the min height of l and r
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_till