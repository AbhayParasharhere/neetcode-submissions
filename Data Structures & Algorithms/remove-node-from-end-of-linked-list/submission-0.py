# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # keep one node spearated by n distacne
        # advacne both until the right node which is ahead reaches the end
        # the before.next node now points to the node to be removed from the end
        # set before.next to before.next.next and boom u are done

        dummy = ListNode(0)
        dummy.next = head
        before = ahead = dummy

        for r in range(n):
            ahead = ahead.next

        # now move both until ahed .next reaches teh end
        # gap bw them is n

        while ahead.next:
            before = before.next
            ahead = ahead.next
        
        # now remove the before.next
        before.next = before.next.next
        return dummy.next
        
