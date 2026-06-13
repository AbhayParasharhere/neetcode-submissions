"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # first we visist all nodes create a copy without random pointers
        # why - otherwise the radom pointer can be pointing to a non existent thing
        # we create deep copy of each node and use a hmpa to store which lists prev node it corresponded to
        # why - this info is useful for ranodm pointer as they are addresses point to but in new list they are diff

        dummy = Node(0)
        dummy.next = head
        hmap = {}

        tailCpy = Node(0)
        cpy = tailCpy

        while head:
            tailCpy.next = Node(head.val)
            hmap[head] = tailCpy.next
            tailCpy = tailCpy.next
            head = head.next
        
        # now cpy.next is a deep copied list
        def printl(l):
            n = l
            while n:
                print(n.val,end=" ")
                n = n.next
        
        hcopy = dummy.next
        ccopy = cpy.next

        while hcopy:
            random = hmap[hcopy.random] if hcopy.random in hmap else None
            ccopy.random = random
            ccopy = ccopy.next
            hcopy = hcopy.next

        return cpy.next
        

