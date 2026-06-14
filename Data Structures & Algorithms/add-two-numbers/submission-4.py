# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = l1
        trail_l1 = dummy
        carry = 0
        # first we add the common parts and carry the carry over

        while l1 and l2:
            tot = math.floor(int(l1.val) + int(l2.val) + carry)
            carry = math.floor(tot/10)
            l1.val = tot % 10
            l1 = l1.next
            l2 = l2.next
            trail_l1 = trail_l1.next
        
        # now we carry the rmeaing list onto l1 which stores our result as well
        # we need to attach remains_head onto l1.next
        remains_head = remains_tail = l1 or l2
        trail_l1.next = remains_head

        while remains_tail:
            tot = math.floor(int(remains_tail.val) + carry)
            carry = math.floor(tot/10)
            remains_tail.val = tot % 10
            remains_tail = remains_tail.next
            trail_l1 = trail_l1.next
        
        # if we have a carry reming in teh end atatch it to trail_l1.next
        if carry != 0: trail_l1.next = ListNode(carry)
        return dummy.next

