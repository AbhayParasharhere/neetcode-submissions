# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # when we reach left tehn we pass everything to a function which would reverse and return teh tail

        def reverse_till(n,count):
            # returns the tail and head of the reversed list
            prev = None
            tail = n
            i = 0
            while i < count and n:
                temp = n.next
                n.next = prev
                prev = n
                n = temp
                i += 1
            return (prev,tail)

        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        at = 1
        while head:
            if at == left:
                # we need to pass to our revrese fx
                # before reversing we need to copy the correpssoding connection after 
                rev_from = pre.next
                for r in range(right-left):
                    if head: 
                        head = head.next
                tail_attach_after = head.next
                h,t = reverse_till(rev_from,right - left + 1)
                # now this tail's next is none we need to change that to its proper location
                pre.next = h
                t.next = tail_attach_after
                at += (right - left) + 1
            head = head.next
            pre = pre.next
            at += 1
        return dummy.next
