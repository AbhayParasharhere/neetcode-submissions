# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # go to the mid of the link list to create a separate second half
        # this second half is reversed to help with your logic
        # finally you construct a list taking one from first list and then from teh second list
        # stcihing them until both list reach the end

        dummy = ListNode(0)
        dummy.next = head

        fast = slow = dummy

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        # now slow.next is start of the second half or true middle in case of odd list
        revFrom = slow.next
        prev = None

        def printl(n):
            cpy = n
            while cpy:
                print(cpy.val,end=" ")
                cpy = cpy.next

        while revFrom:
            temp = revFrom.next
            revFrom.next = prev
            prev = revFrom
            revFrom = temp
        # printl(prev)
        
        # now the final list build where we take from firts then second from rev list
        A = head
        B = prev

        while A.next and B.next:
            tmp1 = A.next
            tmp2 = B.next
            A.next = B
            B.next = tmp1
            A = tmp1
            B = tmp2
        # printl(head)




