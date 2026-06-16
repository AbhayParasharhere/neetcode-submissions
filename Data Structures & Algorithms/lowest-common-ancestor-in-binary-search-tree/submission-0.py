# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # approach 1 - cehck all nodes
        # and the node that satisfies the preoperty being p<=val<=q is teh common ancestor
        # the first nide that satisfies this condition can set the global variable
        # any otehr way to have this passed down as teh eventual asnwer??
        anc = None
        def check(node):
            nonlocal anc
            if not node: return None
            lo, hi = min(p.val,q.val), max(p.val,q.val)
            if node.val >= lo and node.val <= hi:
                anc = node
                return node

            # recurse on left half and right half if not found
            lanc = check(node.left)
            ranc = check(node.right)
            if lanc or ranc: return lanc or ranc
        check(root)
        return anc