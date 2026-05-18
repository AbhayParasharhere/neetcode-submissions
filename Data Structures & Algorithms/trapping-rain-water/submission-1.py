class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0 , len(height) - 1

        maxLeft = height[0]
        maxRight = height[len(height) - 1]
        res = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft,height[l])
                res += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]
        return res
