# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bottom up - postorder
        # as i go up - i return myself to my parent who swaps me with his other child
        # null node returns None as its null

        def invert(node):
            if not node: return None
            lnode = invert(node.left)
            rnode = invert(node.right)
            # swap
            node.left, node.right = rnode, lnode
            return node
        return invert(root)