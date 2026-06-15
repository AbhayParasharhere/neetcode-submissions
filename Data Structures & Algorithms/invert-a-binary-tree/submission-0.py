# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # left node becomes the right and right becomes left
        def invert(node):
            # smallest base case is already inverted
            if not node: return
            # swap the pointers

            # call on left subtree then on right subtree
            # then inorder traversal
            node.left, node.right = node.right, node.left
            invert(node.left)
            invert(node.right)
        invert(root)
        return root