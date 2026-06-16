# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # navigation version
        # we search only the trees necessayr as its a BST
        # if teh node val is greter than lo of our bound we search the left subtree
        # else we search the rt subtree
        # at every point we return teh anc we have found or None
        def anc(node):
            if not node: return None
            cur = node.val
            lo, hi = min(p.val,q.val), max(p.val,q.val)
            if lo <= cur <= hi:
                return node
            elif cur > lo:
                # search the left subtree - its impossible in the rt
                lanc = anc(node.left)
                return lanc
            elif cur < hi:
                ranc = anc(node.right)
                return ranc
        return anc(root)
