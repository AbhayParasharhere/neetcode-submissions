# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(a,b):
            # both became null at the same time
            if not a and not b: return True
            # False if any one those nodes remains
            if (a and not b) or (b and not a): return False

            if a.val != b.val: return False
            else:
                # left and right both must return true for the overall to be true
                return isSame(a.left,b.left) and isSame(a.right,b.right)
        return isSame(p,q)