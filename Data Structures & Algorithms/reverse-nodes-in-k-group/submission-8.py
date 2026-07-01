# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rev_part(node):
            t = node
            i = 0
            prev = None
            while node and i < k:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
                i += 1
            return (prev,t)
        
        dummy = ListNode(0)
        dummy.next = head

        # we keep reversing until our tail trailing pointer exists
        tattach = head
        at = 0
        hattach = dummy
        while tattach:
            at += 1
            tattach = tattach.next
            if at == k:
                h,t = rev_part(hattach.next)
                t.next = tattach
                hattach.next = h
                for r in range(k):
                    if hattach: hattach = hattach.next
                at = 0

        return dummy.next
                