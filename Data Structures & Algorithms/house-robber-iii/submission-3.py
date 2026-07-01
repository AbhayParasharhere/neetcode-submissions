# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # at every node we ask whats teh best if we rob oursself 
        # and if dont choose to rob oursev
        # we return thsi calc back to our parent

        def dfs(node):
            if not node: return (0,0)
            lin,lout = dfs(node.left)
            rin,rout = dfs(node.right)

            # we can only choose the best from our child lout, as child cant be tehre
            mein = lout + rout + node.val
            meout = max(lin,lout) + max(rin,rout)
            return (mein,meout)
        return max(dfs(root))