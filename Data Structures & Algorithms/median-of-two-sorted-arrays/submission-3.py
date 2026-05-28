class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Startegy is to build a valid left side partitoin to return the median
        # This valid left side partion is spit acorss both arrays 
        # It uses a pendlum apporach using m with binary search as a end point
        # which decides hwo many elements from nums 1 and nums 2 to take to form this partition

        # we need half of n as the size of the partiion in the end
        tot = len(nums1) + len(nums2)
        half = tot // 2
        A = nums1
        B = nums2
        if len(B) < len(A):
            A,B = B,A
            # A points to the shorter array always

        l = -1
        r = len(A) - 1 

        while True:
            # we are guaranteed to return a median every time
            m = (l + r) // 2
            n = half - m - 2 # -2 as n is a index taht points to boundary of B 
            # And since both m and n are 0 indexed
            
            Aleft = A[m] if m > -1 else float('-infinity')
            Aright = A[m+1] if m+1 < len(A) else float('infinity')
            Bleft = B[n] if n > -1 else float('-infinity')
            Bright = B[n+1] if n+1 < len(B) else float('infinity')

            if Aleft <= Bright and Bleft <= Aright:
                # Correct partition
                if tot % 2:
                    # odd case
                    return float(min(Aright,Bright))
                return float((max(Aleft,Bleft)+min(Aright,Bright))/2)
            elif Aleft > Bright:
                # We had too many from A so shift m back by shifting r back
                # This automaticallyc hooses more from B due to pendulum approach
                r = m - 1
            else:
                # Case where too many from B
                # Shift m forward by l forward
                l = m + 1