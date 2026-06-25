# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # we nagiuate to the correct branch
        # and when we fidn that node, it retursn its child instade of iteslef back for its parent to attach
        # this is essentially that child removing itself
        # to handle case where left child has both left and rt child
        # and the node to rmeove also has a right child
        # we need to first attach it the left child - rightmost as naturally it would be greateest
        # as its his parent right child which is great than its left

        def delt(node):
            # every ndoe returns addres back to its parent
            # base case null ndoe returns None
            if not node: return None

            # navigate
            if node.val > key:
                # lt subtree somewhre - needs deltion
                node.left = delt(node.left)
                # i return my own address back to parent
                return node
            elif node.val < key:
                node.right = delt(node.right)
                return node
            else:
                # this is the key to delete
                if node.right and node.left:
                    cur = node.left
                    while cur.right:
                        cur = cur.right
                    cur.right = node.right
                    # instead of ndoe we are sending gour child back
                    # :(
                    # /essentially saying delete myself back to parent
                return node.left or node.right
        return delt(root)
