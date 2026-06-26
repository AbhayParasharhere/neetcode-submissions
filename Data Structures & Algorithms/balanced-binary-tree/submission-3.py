# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node: return 0
            return max(height(node.left), height(node.right)) + 1
        
        def balanced(node):
            if not node: return (True,0)
            lb,lh = balanced(node.left)
            rb,rh = balanced(node.right)

            if lb and rb and abs(lh - rh) <= 1:
                # chcek further
                return (lb and rb,max(lh,rh) + 1)
            else:
                return (False,max(lh,rh) + 1)
        
        return balanced(root)[0]