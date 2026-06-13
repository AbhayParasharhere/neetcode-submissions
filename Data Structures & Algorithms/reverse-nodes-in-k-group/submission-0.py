# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # we first advacnce forard by k times - keep a copy of head
        # rveserse from copy and then attach the tail to the advacned head
        # if the advanced head was before k times hit a none - we dont reverse

        def rev(node):
            # returns the head and tail of the node reversed k times
            tail = node
            prev = None
            i = 0
            while node and i < k:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
                i += 1
            return (prev,tail)
        
        dummy = ListNode(0)
        dummy.next = head

        check = head
        hcopy = dummy

        # termination is when the check which says 
        # where the tail of the reversed list will attach to reaches the end
        advance = 0
        while check:
            # advance check k times
            check = check.next
            advance += 1

            # in less than k cases we naturally dont run reverse
            if advance == k:
                # now check is k times ahead so where the tail will attach 
                # and hcopy points to one node before check start
                h,t = rev(hcopy.next)
                # attach the head porpely
                hcopy.next = h
                # attach tail to the advanced pointer check
                t.next = check
                advance = 0
                hcopy = t
        return dummy.next

        
