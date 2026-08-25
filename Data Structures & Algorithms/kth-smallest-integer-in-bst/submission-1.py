# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal returns the elemnets in sorted order in a bst
        # when we reach teh n value equal k return that node value
        res = []
        def inorder(node):
            if not node: return None
            if len(res) == k: return

            inorder(node.left)
            # process
            # print(node.val)
            res.append(node.val)
            inorder(node.right)
        # print(res)
        inorder(root)
        return res[k-1] if res else -1

