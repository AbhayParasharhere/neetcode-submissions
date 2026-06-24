# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 2 important facts allows us to solve this via bottom up or post order
        # why bottom up works better each node builds from tehe ground up
        # retruns its address back to its aprent
        # in top down parent would need to pass - im not sure need to confrim why pre or top down can work or cant
        # teh first value of pre is root
        # anything to teh left till root in inorder is prt of left subtree aything to rt is rt subtree
        # with these 2 principles using indexes we can build the tree
        # a hasmap of val to index for faster lookup of partition
        in_map = {val: i for i, val in enumerate(inorder)}

        def build(pre_st,pre_end,in_st,in_end):
            # we have reached the end, it is a leaf
            if in_st > in_end or pre_st > pre_end:
                return None
            
            root_val = preorder[pre_st]
            partition = in_map[root_val]
            left_size = partition - in_st

            left_pre_st = pre_st + 1
            left_pre_end = left_pre_st + left_size - 1
            right_pre_st = left_pre_end + 1
            right_pre_end = pre_end

            left_in_st = in_st
            left_in_end = in_st + left_size - 1
            right_in_st = left_in_end + 2
            right_in_end = in_end

            node = TreeNode(root_val)
            node.left = build(left_pre_st,left_pre_end,left_in_st,left_in_end)
            node.right = build(right_pre_st,right_pre_end,right_in_st,right_in_end)

            return node
        return build(0,len(preorder) - 1,0, len(inorder) - 1)


