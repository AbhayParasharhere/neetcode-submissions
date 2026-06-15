# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # a reverse fx that reverses a given list k times and returns the head and tail to reconnect
        # we have a trailing pointer that is used to reattach the returned head back
        # this trailing pointer next is advanced k times as the pt to attach teh tail to
        dummy = ListNode(0)
        dummy.next = head

        trailing = dummy
        tailAttach = head
        count = 0

        def rev_from(node):
            t = node
            prev = None
            i = 0
            while node and i < k:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
                i += 1
            return (prev,t)

        while tailAttach:
            tailAttach = tailAttach.next
            count += 1
            if count == k:
                # tail attach to is already at the correct pos
                h,t = rev_from(trailing.next)
                # attach the head and tail of the reverse part
                trailing.next = h
                t.next = tailAttach

                # now need to davance trailing to the correct pos for enxt time
                # which is advacne by k times
                for r in range(k):
                    trailing = trailing.next
                count = 0

        return dummy.next
