# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # bottom up apporach
        # cos every child can return their best asnwer robbing them or without robbing thme
        # parent if choose to rob itself can choose the tup1 entry
        # othersiw without adding themselves the max form both their child entries

        def loot(node):
            # base case null node
            if not node: return (0,0)

            lin,lout = loot(node.left)
            rin,rout = loot(node.right)
            mein = lout + rout + node.val
            # without me in the mix, I can freely choose the 
            # max val from both pair to send to my parent
            meout = max(lin,lout) + max(rin,rout)
            return (mein,meout)
        
        return max(loot(root))
