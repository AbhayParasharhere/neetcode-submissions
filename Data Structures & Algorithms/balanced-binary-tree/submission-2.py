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
            if not node: return True
            lh = height(node.left)
            rh = height(node.right)

            if abs(lh - rh) <= 1:
                # chcek further
                return balanced(node.left) and balanced(node.right)
            else:
                return False
        
        return balanced(root)