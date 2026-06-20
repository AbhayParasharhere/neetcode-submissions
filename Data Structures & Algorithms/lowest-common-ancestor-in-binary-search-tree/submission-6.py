# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we naviaget through the bst by comapring values
        # then through preorder we compare parent value if it satifies teh condition
        # that it is within p and q the nwe early return that node
        # ervy ndoe apart from it returns none otherwise

        def anc(node):
            if not node: return None
            lo, hi = min(p.val,q.val), max(p.val,q.val)
            if lo <= node.val <= hi:
                return node
            elif node.val > lo and node.val > hi:
                # navigate to lt subtree
                return anc(node.left)
            else:
                # navigate to right subtree
                return anc(node.right)
        return anc(root)