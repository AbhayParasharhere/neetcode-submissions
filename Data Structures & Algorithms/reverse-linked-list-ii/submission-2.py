# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        # this reverses a part returns ts head and tail for us to stich later
        def revPart(n,till):
            prev = None
            tail = n
            count = 0
            while n and count < till:
                temp = n.next
                n.next = prev
                prev = n
                n = temp
                count += 1
            return (prev,tail)

        trailing = dummy
        at = 1
        while head:
            if at == left:
                # we use the trailing pointer to stich the returned rev list head
                revFrom = head
                headAttachTo = trailing
                tailAttachTo = head

                for r in range(right-left+1):
                    if tailAttachTo: tailAttachTo = tailAttachTo.next

                h,t = revPart(revFrom,right-left+1)
                
                headAttachTo.next = h
                t.next = tailAttachTo
                at += (right - left) + 1
            at += 1
            head = head.next
            trailing = trailing.next
        return dummy.next
