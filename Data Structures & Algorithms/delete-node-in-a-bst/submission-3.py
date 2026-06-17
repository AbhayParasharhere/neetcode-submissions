# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 2 phases - first search and return teh node foudn that you need to delete
        # if it doesnt exits just return the root

        # phase 2 we need to replace the node with one its children if present
        # if it doesnt have any children we can just remove

        # if we can get the node to remove and its parent then its easy actually
        # atmost 3 stiches needs to be deone to remove the node

        def keyParent(node,parent):
            # if we reach a null node, we return None, None
            if not node: return (None,None)

            # navigate properly to the correct location as per the key
            if node.val > key:
                # search left
                lnode,lpar = keyParent(node.left,node)
                return (lnode,lpar)
            elif node.val < key:
                # search right
                rnode, rpar = keyParent(node.right,node)
                return (rnode,rpar)
            else:
                # equal case
                # print('found',node.val,parent.val)
                return (node,parent)
        node,par = keyParent(root,root)
        if node is None:
            return root
        if node == par:
            # case where root is removed and one child is missing
            # the case where we have both child and root is same as pent is handled already
            # return any child as the 
            if node.left and node.right:
                cur = node.left
                while cur.right:
                    cur = cur.right
                cur.right = node.right
                return node.left              # this IS the new root, correct to return
            return node.left or node.right 

        # print('val',par.val,node.val)
        if par:
            # now see if the node is the left or right val of the parent
            if node.val < par.val:
                if node.left and node.right:
                    par.left = node.left
                    cur = node.left
                    while cur.right:
                        cur = cur.right
                    cur.right = node.right
                elif node.left or node.right:
                    par.left = node.left or node.right 
                else:
                    par.left = None
            else:
                if node.left and node.right:
                    par.right = node.left
                    cur = node.left
                    while cur.right:
                        cur = cur.right
                    cur.right = node.right
                elif node.left or node.right:
                    par.right = node.left or node.right 
                else:
                    par.right = None

        return root


