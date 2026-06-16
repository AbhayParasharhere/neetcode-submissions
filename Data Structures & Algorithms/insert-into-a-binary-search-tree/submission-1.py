# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # we insert the value such that it is at the correct node
        # this node means we navigate correctly going left and right 
        # this correct node must be a leaf such that its left or right checild is none
        # we naviaget based on the node cur value to teh right node for isnertion
        if not root: return TreeNode(val)
        def insert(node):
            # we naivgate to teh lowest leevl which staifies tehn insert there
            if node:
                cur = node.val
                if cur > val:
                    # descend left
                    linsert= insert(node.left)
                    if linsert:
                        # we returned from null child to our left
                        # and it was the correct position so insert at the node left
                        node.left = TreeNode(val)

                elif cur < val:
                    # descend right
                    rinsert = insert(node.right)
                    if rinsert: node.right = TreeNode(val)
                return False
            else:
                return True
        insert(root)
        return root