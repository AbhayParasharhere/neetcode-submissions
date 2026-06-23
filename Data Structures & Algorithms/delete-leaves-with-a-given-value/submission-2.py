# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # every node returns its address to the parent
        # if it equals to the key it deletes itself and retursn the corre
        def deleteKey(node):
            # empty node has empty addres to return its parent base case
            if not node: return None
            node.left = deleteKey(node.left)
            node.right = deleteKey(node.right)
            if node.val == target and not node.left and not node.right:
                return None
            return node
        return deleteKey(root)