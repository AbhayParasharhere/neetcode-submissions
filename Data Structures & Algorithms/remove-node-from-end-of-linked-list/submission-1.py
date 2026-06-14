# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        ahead = before = dummy

        # create gap of n between ahead and before
        for r in range(n):
            if ahead: ahead = ahead.next
        
        # now move both till we dont have ahead.next reaches the end
        # now before.next popints to nth node from the end

        while ahead.next:
            ahead = ahead.next
            before = before.next
        
        # remove the nth ndoe from the end
        before.next = before.next.next

        return dummy.next
