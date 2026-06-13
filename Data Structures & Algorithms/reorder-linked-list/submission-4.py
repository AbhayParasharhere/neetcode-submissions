# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we split the list into 2 parts by half
        # half found by hare algo
        # reverse the other half
        # in the main loop first put the item from the first list then the second stiched tehre
        # do this until you reach the end of both first and second list

        dummy = ListNode(0)
        dummy.next = head
        fast = slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        # slow points to the mid in odd or the first mid in even
        second_half_start = slow
        prev = None

        while second_half_start:
            temp = second_half_start.next
            second_half_start.next = prev
            prev = second_half_start
            second_half_start = temp
        
        # now list is reversed and we have 2 halves that are still connected though
        # but second half is reversed
        first = dummy.next
        second = prev

        while first and second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        print(dummy.next.val)