class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # we get the lsr least smaller to right and least smaller to left 
        # also imp rule is taht smaller can exand into greter bars and can expand till it hits any element smaller that it or the boundary thats why we are intereted in lsr and lsl
        # becuase theya re the blcokers for calcluating teh width at any point i in the arr
        # then formuala is heights[i] * (LSR-LSL - 1)

        n = len(heights)
        def getLSR():
            stack = []
            lsr = [0] * n

            for i in range(n-1,-1,-1):
                # we are calc lsr at ht i right now
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if not stack:
                    lsr[i] = n
                else:
                    lsr[i] = stack[-1]
                # push in stack
                stack.append(i)
            return lsr
        
        def getLSL():
            stack = []
            lsl = [0] * n

            for i in range(0,n):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if not stack:
                    lsl[i] = -1
                else:
                    lsl[i] = stack[-1]
                # push
                stack.append(i)
            return lsl
        
        lsl = getLSL()
        lsr = getLSR()
        width = [0] * n
        ans = 0
        for i in range(n):
            width[i] = lsr[i] - lsl[i] - 1
            area = width[i] * heights[i]
            ans = max(ans,area)
        return ans