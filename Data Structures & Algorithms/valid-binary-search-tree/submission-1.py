# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # using the technique of inorder porducing sorted for BST

        # we can have a prev pointer passed down through recusion to the child, if node val is not greater than prev
        # or strictly in increaing order it is not a BST
        prev = None
        def valid(node):
            nonlocal prev
            if not node: return True
            # propagae to the left side the valid result so far and the prev val
            # pass current val as prev
            lvalid = valid(node.left)
            if not lvalid: return False

            if prev is not None and prev >= node.val: return False
            prev = node.val
            # propogate to the right
            return valid(node.right)
        return valid(root)
        
