# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # in carry case what wouit be be
        #  say 9 - 9 - 4 numbers are 499 + 689 = 1188
        #  say 9 - 8 - 6
        #  then 8 - 8 - 1 - 1
        # we store a carry variable on every sum
        # if we have a carry in the end and is not 0 then we have to create a new node in the end
        # we can store the res in l1 itself

        # we need to point l1 to the greater of the 2 lists 
        l1Cpy = l1
        l2Cpy = l2
        while l1Cpy and l2Cpy:
            l1Cpy = l1Cpy.next
            l2Cpy = l2Cpy.next
        
        if l2Cpy and not l1Cpy:
            l1,l2 = l2,l1
        # every other case we have correct l1 being greater or equal which works

        dummy = ListNode(0)
        dummy.next = l1
        carry = 0
        headCpy = dummy


        while l1 or l2:
            l1_v = l1.val if l1 else 0
            l2_v = l2.val if l2 else 0
            tot = l1_v + l2_v + carry
            # max length of tot is 2 digits
            # we move the first digit to carry if it exist 
            carry = math.floor(tot / 10)
            l1.val = tot % 10 # just get the second digit
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            # a trailing pointer to the tail when l1 reaches the end
            headCpy = headCpy.next
        # print(carry,headCpy.val)
        if carry > 0: headCpy.next = ListNode(carry)
        return dummy.next


        
