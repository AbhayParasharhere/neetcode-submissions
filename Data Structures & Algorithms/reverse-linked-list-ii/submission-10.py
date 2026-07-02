# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = (right - left) + 1

        def rev_part(node):
            t = node
            i = 0
            prev = None
            while node and i < count:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
                i += 1
            return (prev,t)
        
        at = 1
        dummy = ListNode(0)
        dummy.next = head
        hattach = dummy

        while hattach.next:
            if at == left:
                tattach = hattach.next
                for r in range(count):
                    if tattach: tattach = tattach.next

                h,t = rev_part(hattach.next)
                hattach.next = h
                t.next = tattach
                return dummy.next
            at += 1
            hattach = hattach.next
        return dummy.next