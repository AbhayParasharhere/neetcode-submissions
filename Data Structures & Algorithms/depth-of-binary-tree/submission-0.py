# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # depth of node that is a leaf is 1
        # depth of node that is null is 0
        # depth of a node that has both elft and right subtree is the amx of depths from these + 1

        def ht(node):
            if not node: return 0

            ltH = ht(node.left)
            rtH = ht(node.right)
            myH = 1 + max(ltH,rtH)
            return myH
        return ht(root)

