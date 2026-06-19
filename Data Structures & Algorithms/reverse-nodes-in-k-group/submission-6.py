# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # we have a fx that reverses a list and returns the heead and tattach
        # then we stich this head and tailn crrectly
        # we have a counter who is responsibel for calling the fx every k step 
        # if at the end counter is not a multiple of k we dont call this helps us aoid the last chain which might not split evenly into k parts as we dont have to reverse it

        def rev_part(node):
            i = 0
            t = node
            prev = None
            while node and i < k:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
                i += 1
            return (prev,t)
        
        cur = 0
        dummy = ListNode(0)
        dummy.next = head
        hattach = dummy
        tattach = head

        while tattach:
            cur += 1
            tattach = tattach.next
            if cur == k:
                h,t = rev_part(hattach.next)
                t.next = tattach
                hattach.next = h

                # now move hattach forward k times for the next iteration
                for r in range(k):
                    if hattach: hattach = hattach.next
                cur = 0
        return dummy.next



