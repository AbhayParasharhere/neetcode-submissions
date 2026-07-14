# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # do a post order traversal - rpe wont work here as we watn to start
        # removal fromt he bottom
        # if i hit a node iwth no elft and right children its a leaf
        # i then return ull instead of my address back to my parent to delete me

        def solve(node):
            if not node: return None
            node.left = solve(node.left)
            node.right = solve(node.right)
            if node.val == target and not node.left and not node.right:
                return None
            else:
                return node
        return solve(root)