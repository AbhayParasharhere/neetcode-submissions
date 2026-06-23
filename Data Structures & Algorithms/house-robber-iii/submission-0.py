# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # each child returns waht woudl be teh total if it was robbed
        # and it calculates the best total considering his children if it was not robbed
        # by summing the max of their children tuple entries
        # this bottom up approach postorder eventually retursn 2 values
        # 1 - robbed if root was takedn, val if root was not robbed

        def dfs(node):
            # base case for null pointers
            if not node: return (0,0)
            ltuple = dfs(node.left)
            rtuple = dfs(node.right)
            # in case i was robbed then i can only selct tuple entries where my
            # children entreis are not incldues as i cant rob my children if im robbed
            merob = node.val + ltuple[1] + rtuple[1]
            mewithout = max(ltuple) + max(rtuple)
            return (merob,mewithout)
        return max(dfs(root))