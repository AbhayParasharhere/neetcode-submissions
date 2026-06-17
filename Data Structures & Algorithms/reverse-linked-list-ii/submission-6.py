# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # maintian a trailing pointer whose next we will attach the reversed list tail
        # and this trailing pointer next will also advance right - lt + 1 times to the correct pos for head of the rev list to insert
        dummy = ListNode(0)
        dummy.next = head
        trailing = dummy
        tinsert = head
        at = 1
        times = (right - left) + 1

        def rev(node,times):
            t = node
            prev = None
            i = 0
            while node and i < times:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
                i += 1
            return (prev,t)
            
        while tinsert:
            if at == left:
                # advance right - left + 1 of tinsert to get it correctly placed
                for r in range(times):
                    tinsert = tinsert.next
                h,t = rev(trailing.next,times)
                t.next = tinsert
                trailing.next = h
                at += times
                return dummy.next
            tinsert = tinsert.next
            trailing = trailing.next
            at += 1

        return dummy.next