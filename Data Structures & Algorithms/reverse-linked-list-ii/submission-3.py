# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # when we hit left we reverse the portion of the linekd ist get the head and tial of the reervsed scetion
        # we connceted the revserd head to the the prev head next and the tail to connect it we need to first advacne the head pointer propely

        dummy = ListNode(0)
        dummy.next = head

        def rev(node,count):
            tail = node
            prev = None
            i = 1
            while node and i <= count:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
                i += 1
            return (prev,tail)
        at = 1
        l1 = head
        trail = dummy
        while l1:
            if at == left:
                tail = l1
                # advance l1 to right - left + 1 pos as that is where the revresed tail next will be conncted
                for r in range(right-left+1):
                    if tail: tail = tail.next

                h,t = rev(l1,right-left+1)
                trail.next = h
                t.next = tail
                at += right - left + 1
            at += 1
            l1 = l1.next
            trail = trail.next

        return dummy.next

