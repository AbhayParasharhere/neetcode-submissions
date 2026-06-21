# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # we use a top down apporach
        # which is pre order but parent also passes the max val so far found
        # if the value is greater than the max then it is counted as. agood node, otherwise not

        def good(node,maxV):
            # we return the number of good nodes found so far
            if not node: return 0

            meGood = 1 if node.val >= maxV else 0
            if node.val >= maxV: maxV = node.val
            lGood = good(node.left,maxV)
            rGood = good(node.right,maxV)
            # combien the result- pre + postorder style
            return lGood + rGood + meGood
        return good(root,root.val)