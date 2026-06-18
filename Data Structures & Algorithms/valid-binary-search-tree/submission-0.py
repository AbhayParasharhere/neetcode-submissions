# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if its a valid bst than if we do postorder traversal our val shoudl be between left and right
        # if that is not the case we return false

        def valid(node):
            # an empty node is a bst
            # we return each node min and max
            if not node: return (True,float('inf'),float('-inf'))
            l_ok,lmin,lmax = valid(node.left)
            r_ok,rmin,rmax = valid(node.right)
            my_ok = l_ok and r_ok and lmax < node.val < rmin
            my_min = min(node.val,lmin)
            my_max = max(node.val,rmax)
            return (my_ok,my_min,my_max)
        return valid(root)[0]