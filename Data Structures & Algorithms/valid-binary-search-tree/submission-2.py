# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # every parent passes the min and max that it has seen to its child
        # child validates its left and right child values from this
        # we recurse left and rigth same routine
        # every node returns whether its valid or node

        def dfs(node,minm,maxm):
            if not node: return True
            # everything in lt subtree max val is current node
            lvalid = dfs(node.left,minm,node.val)
            # everything in rt subtree mmin value is current onode
            rvalid = dfs(node.right,node.val,maxm)
            mevalid = lvalid and rvalid and node.val < maxm and node.val > minm
            # # need to update minm and maxm as well
            return mevalid
        return dfs(root, float('-inf'), float('inf'))