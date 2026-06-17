# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # first i treid bottom up but ooay for a higher node u can know if its good
        # but nodes above it could also be good node but going bottom up we lose this info
        # instead if we go bottom down, and maintain a max till then, anything down greater than it is a good node

        def good(node,topMax):
            # the return value is number of good nodes
            if not node: return 0
            localMax = max(node.val,topMax)
            selfCount = 1 if node.val >= localMax else 0
            lGoodNodes = good(node.left,localMax)
            rGoodNodes = good(node.right,localMax)
            return selfCount + lGoodNodes + rGoodNodes
            
            

        return good(root,root.val)         
