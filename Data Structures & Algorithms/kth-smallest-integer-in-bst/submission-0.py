# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        at = 1
        res = None

        # inorder traversal gets the tree in sorted order
        def getk(node):
            nonlocal at
            nonlocal k
            nonlocal res
            if not node: return None
            getk(node.left)
            if at == k:
                res = node.val
            at += 1
            getk(node.right)
        getk(root)
        return res