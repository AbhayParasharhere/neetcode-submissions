class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # we use the logic wher we find teh lefttmost patrioin boundary
        # that would have formed had both array been merged porely
        # we use a see saw approach using binary search in the shorter sarray
        # to be able to find boundaries in both array of the leftmost part

        A = nums1
        B = nums2

        if len(B) < len(A): A,B = B,A

        half = (len(nums1) + len(nums2))//2

        l = -1
        r = len(A) - 1

        while True:
            m = (l+r) //2
            n = half - m - 2 # -2 as both m and n are 0 indexed 

            Alt= A[m] if m >= 0 else float('-infinity')
            Art= A[m+1] if m + 1 < len(A) else float ('infinity')
            Blt= B[n] if n >= 0 else float('-infinity')
            Brt= B[n+1] if n + 1 < len(B) else float ('infinity')

            if Alt <= Brt and Blt <= Art:
                # valid left partition both places
                if (len(nums1) + len(nums2)) % 2:
                    # odd
                    return float(min(Art,Brt))
                return float((max(Alt,Blt) + min(Art,Brt))/2)
            elif Alt > Brt:
                # More from A so move m back by shiting r back
                r = m - 1
            else:
                # more from B so shift m forawad to take more from A less from B
                l = m + 1
        