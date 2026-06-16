# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # post order variant of search every node 
        # until node that satisfies the bw p and q property

        def check(node):
            if not node: return None
            lanc = check(node.left)
            ranc = check(node.right)
            myanc = node.val
            lo, hi = min(p.val,q.val), max(p.val,q.val)
            if lo <= myanc <= hi:
                return node
            # else we use the ancestor of our children
            return lanc or ranc
        return check(root)
