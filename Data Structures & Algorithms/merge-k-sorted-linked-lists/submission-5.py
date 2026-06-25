# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # we mege two lists at the l and r pointer and put the result in the l location
        # we complete half the list when l becomes > r
        # we continue this logratihmic division until list is singular
        # every l pos in the list contributes or is merged only logn times
        # so complex is logn 
        if not lists: return None
        def mergeTwo(l1,l2):
            res = ListNode(0)
            h = res
            while l1 and l2:
                if l1.val <= l2.val:
                    res.next = l1
                    l1 = l1.next
                else:
                    res.next = l2
                    l2 = l2.next
                res = res.next
            # stich the remainder
            res.next = l1 or l2
            return h.next

        n = len(lists)
        # continue until our halving reaches a singular list
        while n > 1:
            l = 0
            r = n -1
            while l < r:
                lists[l] = mergeTwo(lists[l],lists[r])
                l += 1
                r -= 1
            n = math.ceil(n/2)
        return lists[0]
