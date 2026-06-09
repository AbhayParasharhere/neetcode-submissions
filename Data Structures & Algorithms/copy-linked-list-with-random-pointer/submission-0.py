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
        # 2 pass soution
        # first copy every node in another res list without random
        # then in second pass copy the random pointer where it points to

        def printl(n):
            while n:
                print(n.val, " ", n.random.val if n.random else "None")
                n = n.next
        # start
        if not head: return None

        dummy = Node(-1000)
        dummy.next = head

        cpyHead = cpy = Node(head.val)
        headCpy = head
        # keep track of index to node cpy ration to copy random easily in next pass
        imap = {headCpy: cpy}

        while headCpy.next:
            # need to create the next node
            cpy.next = Node(headCpy.next.val)
            cpy = cpy.next
            headCpy = headCpy.next
            imap[headCpy] = cpy

        headCpy = head
        resHead = cpyHead
        while headCpy:
            rand = headCpy.random 
            if rand in imap:
                resHead.random = imap[rand]
            headCpy = headCpy.next
            resHead = resHead.next

        return cpyHead
        
