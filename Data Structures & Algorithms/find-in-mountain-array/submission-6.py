class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # First find the mountain index which acts as a partiton point
        # then comapre it to target to find the right partion to search

        # Mountain aprtiton first true is such that the element eo the right is less
        n = mountainArr.length()
        l = 0
        r = n

        while l < r:
            m = (l+r) //2
            nxt = mountainArr.get(m+1) if m + 1 < n else float('-infinity')
            at = mountainArr.get(m) if m < n else float('-infinity')
            if nxt < at: r = m
            else: l = m + 1
        
        mn = l
        # print(mn)

        def bsAsc(l,r):
            print('asc',l,r,mn)
            bound = r
            while l < r:
                m = (l+r) // 2
                if mountainArr.get(m) >= target: r= m
                else: l = m + 1
            if l < n and (l == mn + 1 or target != mountainArr.get(l)): return -1
            return l
        
        def bsDsc(l,r):
            print('dsc',l,r)
            bound = r
            while l < r:
                m = (l+r) // 2
                if mountainArr.get(m) <= target: r = m
                else: l = m + 1
            if l < n and (l == mn or target != mountainArr.get(l)): return -1
            return l
        
        ascRes = bsAsc(0,mn+1)
        if ascRes == -1:
            return bsDsc(mn+1,n)
        else: 
            return ascRes

