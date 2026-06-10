class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # we use a binary search to find the position of a point in the shoter array
        # usch that we have a unified left half where elements in nums 2 left are strictly less than nums 1 right
        # elemenst in nums 1 left are strictly less than nums 2 right - taht is we find the overall half
        # as if nums was combined, we usea. seesaw apporach as mid shift in shorter array teh elements from the otehr arrya are also pciked diffrently
        
        A, B = nums1, nums2
        tot = len(A) + len(B)
        half = tot // 2

        if len(B) < len(A): A,B = B,A
        # swap so now A is guaranteed shorter
        # we start from 1 before the start and 1 after the end

        l = -1
        r = len(A) - 1
        # note l starts at -1 cos we are using m directly for left elemnet access
        # r starts at len -1 cos we are doing m + 1 so last is technically still at len(A) which is 1 after last index
        
        while(True):
            m = (l + r) // 2
            n = half - m - 2 # -2 as both m and n are 0 indexed

            Alt = A[m] if m >= 0 else float('-infinity')
            Art = A[m+1] if m + 1 < len(A) else float('infinity')
            Blt = B[n] if n >= 0 else float('-infinity')
            Brt = B[n+1] if n + 1 < len(B) else float('infinity')

            if Alt <= Brt and Blt <= Art:
                if tot % 2:
                    return min(Art,Brt)
                else:
                    return (max(Alt,Blt) + min(Art,Brt)) / 2
            elif Alt > Brt:
                # need less element from A shift m back by shifting r back
                r = m - 1
            else:
                # need less from B, more from A shift l forward
                l = m + 1
        