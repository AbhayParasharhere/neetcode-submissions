# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(node):
            # null is balanced yes. we track height as well which is 0 here for null
            if not node: return (0,True)
            lth,ltb = balanced(node.left)
            rth,rtb = balanced(node.right)

            myh = max(lth,rth) + 1
            myb = abs(lth - rth) <= 1 and abs(lth - rth) >= 0
            if not ltb or not rtb:
                myb = False
            
            return (myh,myb)
        
        return balanced(root)[1]
