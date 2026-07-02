# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # every node calc its diameter beased on best diamenter returned from its left and right diam
        # it picks the best of them and returns it back
        # it calc its own diameter by using max of height of its right an dleft and adding 1
        # this diameter is where node is used in calcl
        # the other treurned value is the best diameter where its not icnldued but only from its right and left half alc

        def dfs(node):
            if not node: return(0,0)
            lht, ld = dfs(node.left)
            rht, rd = dfs(node.right)
            myh = max(lht,rht) + 1
            myd = max(ld,rd, lht + rht)
            return (myh,myd)
        return dfs(root)[1]