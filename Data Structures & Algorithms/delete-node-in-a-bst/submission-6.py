# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delt(node):
            # in case of none nothing to attach
            if not node: return None
            if node.val > key:
                node.left = delt(node.left)
                return node
            elif node.val < key:
                node.right = delt(node.right)
                return node
            else:
                if node.left and node.right:
                    # key node has both childs left and right
                    # we send the left node to be attached to our parent
                    # but to not abandon my right child need to attach it to my left child rightmost
                    # need to attach it to my left most child right elem
                    cur = node.left
                    while cur.right:
                        cur = cur.right
                    cur.right = node.right
                    return node.left
                elif node.left or node.right:
                    # in case key node has 1 child just attach that single child
                    return node.left or node.right
                else:
                    # in case key node has no child, None is to be attached
                    return None
        return delt(root)