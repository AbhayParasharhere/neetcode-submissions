class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # so bsaiclly what we need is the left half of the overall sorted array
        # if we have the overall sorted left half liek where it starts and ends in both sorted array
        # wee esenitaly have the merged list sorted and we can get the median easily knwoing this boudnary
        # to get this boudnary we can use binray search witha see saw apporach
        # basic idea is in nums1 or A or shorter array our boundary last element should be less than the 
        # sorted array B bounded elemets boudnary's next element
        # similary B boundary end should be less than A boudnary end whatver we calc
        # to get these boudnary level in 1 using bs we use a seesaw appraoch as both in total have exactly half the elements of the both array

        tot = len(nums1) + len(nums2)
        half = tot // 2

        A,B = nums1,nums2
        if len(nums2) < len(nums1):
            A,B = B, A
        n = len(A)
        l = -1
        r = n

        # as gurantee median exits we must return
        while True:
            m = (l+r) // 2
            AendIdx = m
            BendIdx = half - m - 2 #2 cos both a and b idx are 0 indexed and half is quantity 1 indexed

            Alt = A[AendIdx] if AendIdx >= 0 else float('-inf')
            Art = A[AendIdx+1] if AendIdx+1 < len(A) else float('inf')
            Blt = B[BendIdx] if BendIdx >= 0 else float('-inf')
            Brt = B[BendIdx + 1] if BendIdx + 1 < len(B) else float('inf')

            if Alt <= Brt and Blt <= Art:
                # right partition condition reached in both through see saw
                if tot%2:
                    # odd case, we return the min of the brt,art
                    return min(Art,Brt)
                return (max(Alt,Blt) + min(Art,Brt)) / 2
            elif Alt > Brt:
                # we must move back on A by moving r back
                r = m -1
            else:
                # we must move B end forward by moving l forward
                l = m + 1
                

                    
            
