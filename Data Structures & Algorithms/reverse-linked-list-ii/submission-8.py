# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = (right - left) + 1

        # reatrusn teh h,t of teh reversed part
        def rev_part(node):
            prev = None
            tail = node
            i = 0
            while node and i < count:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
                i += 1
            return (prev,tail)

        dummy = ListNode(0)
        dummy.next = head
        trailing = dummy
        at = 1

        while trailing:
            if at == left:
                # advance tail forwards to correct place to reattach
                tail_attach = trailing.next
                head_attach = trailing
                for r in range(count):
                    if tail_attach: tail_attach = tail_attach.next
                h,t = rev_part(trailing.next)
                head_attach.next = h
                t.next = tail_attach
                return dummy.next
            trailing = trailing.next
            at += 1
        