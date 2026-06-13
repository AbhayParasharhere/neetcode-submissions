# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # have a genreic merge 2 linked list fx and put the result at the l pointer
        # the lr pointer move logara=himally such that the accumualtion of right half is in the lfft half sorted
        # we keep sorting by half until we have one list 

        n = len(lists)
        if n <= 0: return None
        def merge(l1,l2):
            res = ListNode(0)
            head = res
            while l1 and l2:
                if l1.val <= l2.val:
                    res.next = l1
                    l1 = l1.next
                else:
                    res.next = l2
                    l2 = l2.next
                res = res.next
            res.next = l1 or l2
            return head.next
        
        # now logarithimally call with l r pointers
        l = 0
        r = n - 1

        while n != 1:
            while l < r:
                lists[l] = merge(lists[l],lists[r])
                l += 1
                r -= 1
            n = math.ceil(n/2)
            l = 0
            r = n - 1
        return lists[0]
