# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # bottom up apporach + preorder to count itself as we need whetehr aprent is good or not
        # every child returns the good nodes until its level
        # but parent also counts itself
        # parent also return teh max he has seen to his children

        def good(node,max_from_top):
            # base case null node, its definiely not good
            if not node: return 0

            megood = 1 if node.val >= max_from_top else 0
            # update max for my children downwards
            max_from_top = max(max_from_top,node.val)
            lgood = good(node.left, max_from_top)
            rgood = good(node.right, max_from_top)

            # postorder combine step
            # for me all my good nodes back to my parent are all my left chil goo dnode + rchidl nodes
            # + if im a good node or not
            return megood + lgood + rgood
        return good(root,root.val)