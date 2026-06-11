class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # first need to find the mountain which is tahe partition point
        # everything after moountain is less than it

        # Monotonic condition is that element to its left is greater than the elemnt
        # mountain is the first true of this monotonicity

        n = mountainArr.length()
        l = 0
        r = n

        while l < r:
            m = (l+r) // 2
            lt = mountainArr.get(m-1) if m-1 >= 0 else float('-infinity')
            at = mountainArr.get(m)
            if at <= lt: r = m
            else: l = m + 1
        
        mountain = l - 1

        # print(l-1,mountainArr.get(l-1))

        def bs(l,r):
            bound = r
            while l < r:
                m = (l + r) // 2
                if mountainArr.get(m) >= target: r = m
                else: l = m + 1
            if l == bound: return -1
            return l if mountainArr.get(l) == target else -1
        
        def bs_dsc(l,r):
            bound = r
            while l < r:
                m = (l+r) // 2
                if mountainArr.get(m) <= target: r = m
                else: l = m + 1
            if l == bound: return -1
            return l if mountainArr.get(l) == target else -1
            
        res = bs(0,mountain)
        if res == -1:
            res = bs_dsc(mountain,n)
        
        return res

