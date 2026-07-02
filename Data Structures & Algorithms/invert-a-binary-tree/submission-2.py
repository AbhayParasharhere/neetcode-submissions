# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # every ndoe returns its address back to its parent
        # if im a node and i have left and right child
        # i swap them and return my address back to my parent
        # base case - returns none

        def dfs(node):
            if not node: return None
            # swap my current child
            node.left, node.right = node.right, node.left
            # recursively swap eveyrthing in my left subtree
            dfs(node.left)
            # recusively swap eveything in my rt subtree
            dfs(node.right)
            return node
        return dfs(root)