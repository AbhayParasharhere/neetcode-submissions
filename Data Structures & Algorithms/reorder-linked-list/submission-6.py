# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # the reordeing is done as follow
        # first we find the lower mid in case of odd, or frist mid in case of even
        # then we reverse the list after that mid point
        # why - cos we need to put the elem from the end in the start that is go backwards in lilnekdin list best way is to reverse till that
        # then we proceed on building main list
        # this is done by stiching the first elem from the orginal list then the second 
        # element fromt he reversed list then again advacnibgf irst and so on

        dummy = ListNode(0)
        dummy.next = head
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        mStart = slow
        revFrom = slow.next

        # cleanly cut the first half from the seond half which needs revesing
        mStart.next = None
        prev = None
        while revFrom:
            temp = revFrom.next
            revFrom.next  = prev
            prev = revFrom
            revFrom = temp
        
        # now we have 2 separate lists 
        A = dummy.next
        B = prev

        while A and B:
            temp1 = A.next
            temp2 = B.next
            A.next = B
            B.next = temp1
            A = temp1
            B = temp2
