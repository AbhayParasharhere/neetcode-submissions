class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Strategy first get the mountain index
        # AFter we have the mountain index first seach in teh increasing seq on the left
        # Then if not found and returned from the left search to the right of the mountain
        # To get the mountain, mountain and all its elements after it 
        # statisfy the conditon that tehir lement to the right if exits is less than them
        # return the first true thats teh mountain 
        # then go from there
        n = mountainArr.length()
        l = 0
        r = n

        while l < r:
            m = (l + r) // 2
            if m+ 1 < n and mountainArr.get(m) > mountainArr.get(m+1):
                r = m
            else: l = m + 1
        # Now we have mountain at l
        # print(l)
        mountain = l

        # Case for mountain search
        if mountainArr.get(mountain) == target: return mountain

        # First search the increasing half
        def bsAsc(l,r):
            while l < r:
                m = (l+r) //2
                if mountainArr.get(m) >= target: r = m
                else: l = m + 1
            if l == mountain or mountainArr.get(l) != target: return -1
            return l
        
        # Helper for search in decreasing half
        # Uses last false here
        def bsDsc(l,r):
            print('searched dsc')
            while l < r:
                m = (l+r) //2
                if mountainArr.get(m) < target: r = m
                else: l = m + 1
            if l < 0: return -1
            if mountainArr.get(l-1) != target: return -1
            return l - 1
        
        # call relevant helper based on target
        asc = bsAsc(0,mountain)
        # print('asc val',asc)
        if asc == -1:
            if mountain + 1 < n:
                dsc = bsDsc(mountain+1,n)
                if mountainArr.get(dsc) != target:
                    return -1
                return dsc
            else: return -1
        else:
            if mountainArr.get(asc) != target:
                return -1
            return asc

