# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # we use a bottom up approach
        # eachnode retrnsits address abck to its parents
        # each ndoe recives its own preorder and inorder indexes to help them know 
        # which is the rorot and which are their left and right subtree
        # the most im things are- first elem in preorder is always root
        # elem to the left until we find that root in inorder are part of the left subtree
        # leme tot this partition to the right are part of the right subtree

        # inmap for faster lookup of parition
        in_map = {val:i for i,val in enumerate(inorder)}

        def build(pre_st,pre_end,in_st,in_end):
            # when our bounds are crossed, we have reached the null portion nodes
            if in_st > in_end:
                return None
            root_val = preorder[pre_st]
            partition = in_map[root_val]

            # now we have the partition we can calculat the left size to help with 
            # what ghoes to our lf and rt subtree
            left_size = partition - in_st
            lt_pre_st = pre_st + 1
            lt_pre_end = lt_pre_st + left_size - 1
            lt_in_st = in_st
            lt_in_end = in_st + left_size - 1

            rt_pre_st = lt_pre_end + 1
            rt_pre_end = pre_end
            rt_in_st = lt_in_end + 2
            rt_in_end = in_end

            n = TreeNode(root_val)
            n.left = build(lt_pre_st,lt_pre_end,lt_in_st,lt_in_end)
            n.right = build(rt_pre_st,rt_pre_end,rt_in_st,rt_in_end)

            return n
        return build(0,len(preorder)-1,0,len(inorder) - 1)
            
