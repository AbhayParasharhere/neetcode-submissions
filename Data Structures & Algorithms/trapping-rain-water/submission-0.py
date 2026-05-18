class Solution:
    def trap(self, height: List[int]) -> int:
        # at each position the water trapped is = height[i] - min(maxLeft from i,maxright from i)
        # Using o n sapce approch
        # Im using inclusive approach so max left at i includes height i into consideratiopn
        n = len(height)
        maxLeft = [0 for _ in range(n)]
        maxRight = [0 for _ in range(n)]

        if not height: return 0
        soFar = height[0]
        for i in range(n):
            if height[i] > soFar:
                soFar = height[i]
            maxLeft[i] = soFar
        
        # Now fill the max Right
        soFar = height[n-1]

        for i in range(n-1,-1,-1):
            if height[i] > soFar:
                soFar = height[i]
            maxRight[i] = soFar
        
        # Now get the res using the formula -
        # water trapped at i is min(maxLeftSoFar,maxRightSoFar) - height[i]
        res = 0
        for i in range(n):
            res += min(maxLeft[i],maxRight[i]) - height[i]
        return res