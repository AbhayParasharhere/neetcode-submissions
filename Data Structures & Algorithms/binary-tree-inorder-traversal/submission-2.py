# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        stack = []
        res = []

        while cur or stack:
            # first we are intrested in going to the leftmost
            # while storing the ancestros in stack as we need to vist them later
            while cur and cur.left:
                # store ancestor
                stack.append(cur)
                cur = cur.left
            # now we process the cur on top of tsack
            if not cur: cur = stack.pop()
            res.append(cur.val)
            # now try to go to the right if available 
            # worst case cur becomes null we go back to one of those ancestors
            # else in eevry ancestor or left node we always look to the right 
            # after vewing evyerhting to our left
            cur = cur.right
        return res
        
