# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # post order bottom up apporach - 
        # note top down can also work when we navigate to the correct element to remove
        # we have to look at the child and do the stiching ourselves later
        # slighlt more complex but a bit faster
        # in bottom up apporach every node return its address back to the parent
        # the node is amrt enough to know if it is the one being removed
        # in thtat case it sends the left child as its replacemnt and attaches its org
        # rt child to its left child leftmost right node

        def deleteN(node):
            if not node: return None

            # navigate properly as its a bst
            if node.val > key:
                # nav left subtree
                # parent inserts what its child returns
                # most child return themselves the deleted one manages and returns the correct tree
                node.left = deleteN(node.left)
                return node
            elif node.val < key:
                # nav rt subtree
                node.right = deleteN(node.right)
                return node
            else:
                # its tehe key node so must delete propely
                cur = node.left
                while cur and cur.right:
                    cur = cur.right
                if cur: cur.right = node.right
                # returning node.left instead of node itself essentially we are deleting node val
                # or condition for cases where we dont have a left child in that case just simple right child reattach
                return node.left or node.right
        # eventually we bubble up to root correctly
        return deleteN(root)
