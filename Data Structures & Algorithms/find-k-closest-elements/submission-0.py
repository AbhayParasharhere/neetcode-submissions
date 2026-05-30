class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # BS to find the correct palcement that could have been of the x
        # then throiugh two pointer grab teh closest k element

        l = 0
        r = len(arr)
        res = []

        while l < r:
            m = (l+r) // 2
            if arr[m] >= x: r = m
            else: l = m + 1
    
        # Now need to grab k elements 
        # At every point we compare element at l to elemnt after and before it
        # out of those 3 the minimum diff to target gets pushed to res
        # l also moves in taht diretcion
        lo = l -1
        hi = l
        while len(res) < k:
            before = arr[lo] if lo >= 0 else float('infinity')
            after = arr[hi] if hi < len(arr) else float('infinity')

            if abs(before - x) <= abs(after - x):
                # move the before pointer
                res.append(before)
                lo -= 1
            else:
                res.append(after)
                hi += 1

        return arr[lo+1 : hi]