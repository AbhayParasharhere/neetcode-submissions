# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diamater of tree with null is 0
        #          of tree with no leaf is 1
        #          of tree with a left and right tree could be its height which is 1 + lft and reight rtree height
        #  or it could be max of whatsver diamater we get from teh left tree or the right tree + 1

        def diam(node):
            # h 0 d
            if not node: return(0,0)
            lth, ltd = diam(node.left)
            rth, rtd = diam(node.right)
            myht = max(lth,rth) + 1
            myd = max(lth + rth,ltd,rtd)
            return (myht,myd)

        return diam(root)[1]