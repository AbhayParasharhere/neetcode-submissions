# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # again bottom up appoarch why - parent calculates its diameter based on its left and rt children ht
        # and the max diamter so far in their child - so we need tupel height and diameter
        # formual for diam = max(rdiam,ldiam,rtht+ltht) ht starts from 1 when there is a node 0 otherwise
        # as a child my responsibility for my parent is to calculate my own diamter max and my own ht and pass to parent
        def diam(node):
            if not node: return(0,0)
            ld,lh = diam(node.left)
            rd,rh = diam(node.right)
            myh = max(lh,rh) + 1
            myd = max(ld,rd,rh+lh)
            # propogate to the parent
            return (myd,myh)

        return diam(root)[0]

