# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # at every node, tehre are 4 path variants
        # 1st is node + left subtree descending path
        # 2nd is node + rt subtree decending path
        # 3rd is node + lt node + rt node both included descending path
        # 4th is just that node itself
        # we use a non local res that keeps track of the maxium of every possible path
        # the idea is that we iwll be checking all possible path, and max is assigned to the max of them
        res = float('-inf')
        def path(node):
            nonlocal res
            if not node: return (float('-inf'),float('-inf'),float('-inf'),float('-inf'))
            # ltDescend,rtDescend,bothDescend,nodeonly

            ltuple = path(node.left)
            rtuple = path(node.right)
            
            l_attach = max(ltuple[0],ltuple[1],ltuple[3])
            r_attach = max(rtuple[0],rtuple[1],rtuple[3])

            ltDescent = node.val + l_attach
            rtDescent = node.val + r_attach
            bothDescent = node.val + l_attach + r_attach
            nodeonly = node.val

            res = max(res,ltDescent,rtDescent, bothDescent, nodeonly)
            return (ltDescent,rtDescent,bothDescent,nodeonly)
        path(root)
        return res



