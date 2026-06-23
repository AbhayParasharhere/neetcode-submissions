"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isGridIdentical(r_start,r_end,c_start,c_end):
            # print(r_start,r_end,c_start,c_end)
            cmp = grid[r_start][c_start]
            for i in range(r_start,r_end + 1):
                for j in range(c_start, c_end + 1):
                    if i == 0 and j == 0: continue
                    elm2check = grid[i][j]
                    if cmp != elm2check:
                        return (False,0)
            return (True,cmp)

        def build(r_start,r_end,c_start,c_end):
            if r_start > r_end or c_start > c_end: return
            cmp,r_val = isGridIdentical(r_start,r_end,c_start,c_end)
            if cmp:
                return Node(r_val,1,None,None,None,None)
            else:
                # we need to divide the grid equally by 4 and recurse
                # every node returns its address back to its parent
                # postorder bottom up
                r_mid = (r_start + r_end) // 2
                c_mid = (c_start + c_end) // 2
                node = Node(r_val,0,None,None,None,None)
                node.topLeft = build(r_start,r_mid,c_start,c_mid)
                node.topRight = build(r_start,r_mid,c_mid + 1,c_end )
                node.bottomLeft = build(r_mid + 1, r_end,c_start,c_mid)
                node.bottomRight = build(r_mid + 1, r_end,c_mid + 1,c_end)
                return node
        return build(0,len(grid) - 1, 0, len(grid[0]) - 1)