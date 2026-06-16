# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # iterative variant using a pre order dfs
        stack = [root]
        lo, hi = min(p.val,q.val), max(p.val,q.val)
        res = None
        while stack:
            node = stack.pop()
            cur = node.val
            if lo <= cur <= hi:
                res = node
            elif cur > lo:
                # we wnat to search the left subtree
                stack.append(node.left)
            else:
                stack.append(node.right)
        return res