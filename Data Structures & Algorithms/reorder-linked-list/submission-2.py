# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # have one pointer at end of list and another fast one would be at the end
        dummy = ListNode(0)
        dummy.next = head

        slow = fast = dummy
        count = 0

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        
        # now slow next points to the second middle element in an even list

        # now we reverse the next pointer order as we want r to move back
        # we do this from slow.next node till the end
        rev_from = slow.next
        prev = None # instead of null

        while rev_from:
            temp = rev_from.next
            rev_from.next = prev
            prev = rev_from
            rev_from = temp

        slow.next = None
        # Now wae have two clean halves
        # now we build teh final list 
        first = head
        second = prev

        while first.next and second.next:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            # advance first
            first = temp1 # as second occupies the first next
            # or we can write
            # first = first.next
            second = temp2
        first.next = second


