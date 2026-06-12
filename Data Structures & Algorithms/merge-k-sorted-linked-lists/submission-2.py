# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # approach -
        # we take two pointer one at start and another at end while l < r or we pass to form a ocomplete sorted list
        # we assign l = 0 as the result initally and then
        # we sort these 2 sorted list and put the result in our final linked list
        # continue we have a whole sorted linked list
        if len(lists) <= 0: return None

        final = ListNode(0) # final linked list

        def sort_res_with_end(res,end):
            dummy = ListNode(0)
            tail = dummy
            while res and end:
                if res.val <= end.val:
                    tail.next = res
                    res = res.next
                else:
                    # attach this after res
                    tail.next = end
                    end = end.next
                tail = tail.next
            tail.next = res or end
            res = dummy.next
            return res

        n = len(lists)
        l = 0
        r = n - 1
        
        # log n ops per list
        while n != 1:
            # merge and sort the lists at the end of 2 pointer
            while l < r:
                lists[l] = sort_res_with_end(lists[l],lists[r])
                r -= 1
                l += 1
            n = (n + 1) // 2
            l = 0
            r = n - 1

        return lists[0]



