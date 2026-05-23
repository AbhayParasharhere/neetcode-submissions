class Solution:
    def mySqrt(self, x: int) -> int:
        # Square root falls bewteen 0 and n of that number
        l, r = 0, x + 1

        while l < r:
            m = (l+r) //2
            if m * m > x: r = m
            else: l = m + 1
        
        return l -1