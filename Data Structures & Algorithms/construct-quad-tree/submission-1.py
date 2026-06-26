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
        # divide and conquer where we have a fx which checks if a grid of a size is identiical
        # if its not we divide the array into 4 segments acorss rows and cols
        # then check thse 4 segments recusievly
        # if a segment is identical then we have our base case of is leaf and whatver value

        # inclusive of r_st and r_end
        def isGridSame(r_st,r_end,c_st,c_end):
            check = grid[r_st][c_st]

            for r in range(r_st,r_end+1):
                for c in range(c_st,c_end+1):
                    if r == r_st and c == c_st: continue
                    if grid[r][c] != check: return False
            return True
        
        # every node returns its address back to its parent to build
        def build(r_st,r_end,c_st,c_end):
            if isGridSame(r_st,r_end,c_st,c_end):
                # a leaf as its identical
                val = grid[r_st][c_st]
                return Node(val,1,None,None,None,None)
            m_row = (r_end + r_st) // 2
            m_col = (c_end + c_st) // 2

            # not a leaf so any value is fine say 1
            n = Node(1,0,None,None,None,None)
            n.topLeft = build(r_st,m_row,c_st,m_col)
            n.topRight = build(r_st,m_row,m_col+1,c_end)
            n.bottomLeft = build(m_row+1,r_end,c_st,m_col)
            n.bottomRight = build(m_row+1,r_end,m_col+1,c_end)
            return n

        return build(0,len(grid)-1,0,len(grid[0]) - 1)
